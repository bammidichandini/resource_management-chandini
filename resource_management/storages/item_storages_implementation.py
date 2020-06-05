from abc import ABC
from abc import abstractmethod
from typing import List
from resource_management.dtos.dtos import(
    ItemDto,
    UserDto,
    RequestsDto,
    ResourceItemDto,
    itemdto,
    userdto,
    ResourceItemParametersDto
    )
from resource_management.models import (
    Resource,
    User,
    Item
    )
from resource_management.models.item import (
    UserAccess,
    Request
    )
from django.db.models import Prefetch
from resource_management.interactors.storages.item_storages import \
    StorageInterface
from resource_management.exceptions.exceptions import(
    UserCannotManipulateException,
    InvalidDetailsException,
    InvalidIdException
    )



class StorageImplementation(StorageInterface):

    def create_item(
        self,
        item_dto: ItemDto,
        user_id: int
        ):
        resource = Resource.objects.get(name=item_dto.resource_name)
        user = User.objects.get(id=user_id)
        item = Item.objects.create(
            name=item_dto.item_name,
            link=item_dto.link,
            resource=resource,
            description=item_dto.description,
            )
        UserAccess.objects.create(
            item_id=item.id,
            user=user
        )



    def delete_items(
        self,
        item_ids_list: List[int],
        user_id: int
        ):

        Item.objects.filter(id__in=item_ids_list).delete()


    def update_item(
        self,
        item_id: int,
        item_dto: ItemDto,
        user_id: int
        ):
        resource = Resource.objects.get(name=item_dto.resource_name)
        Item.objects.filter(
            id=item_id
            ).update(
                name=item_dto.item_name,
                link=item_dto.link,
                resource=resource,
                description=item_dto.description
                )
        # UserAccess.objects.filter(item_id=item_id, user_id=user_id).\
        #     update(access_level=item_dto.access_level)


    def is_admin(self, user_id: int) -> List[int]:
        is_admin = User.objects.get(id=user_id).is_admin
        return is_admin


    def get_resource_items(self, req_param_dto : ResourceItemParametersDto)\
                    -> ResourceItemDto:

        resource_id = req_param_dto.resource_id
        offset = req_param_dto.offset
        limit = req_param_dto.limit
        item_objs = Item.objects.filter(resource_id=resource_id)[offset:offset+limit]
        item_dto_list = self.convert_and_get_item_dto_objs_list(
            item_objs=item_objs,
            resource_id=resource_id
            )
        return item_dto_list

    @staticmethod
    def convert_and_get_item_dto_objs_list(
        item_objs,
        resource_id
        ):
        resource = Resource.objects.get(id=resource_id)
        count = len(list(Item.objects.filter(resource_id=resource_id)))
        item_dto_list = []
        Item.objects.all()
        for item_obj in item_objs:
            item_dto_list.append(
                itemdto(
                item_id=item_obj.id,
                item_name=item_obj.name,
                link=item_obj.link,
                description=item_obj.description
                )
                )
        resource_dto = ResourceItemDto(
            id=resource.id,
            resource_name=resource.name,
            description=resource.description,
            link=resource.link,
            items_count=count,
            image_url=resource.image_url,
            item=item_dto_list
            )
        return resource_dto


    def get_users_for_items(
        self,
        item_id: int,
        offset: int,
        limit: int
        ) -> List[UserDto]:

        item = Item.objects.get(id=item_id)
        count = len(list(UserAccess.objects.prefetch_related('user').filter(item_id=item.id).\
            values('access_level','user__username','user__department','user__job_role')))
        userobjects = UserAccess.objects.prefetch_related('user').filter(item_id=item.id).\
            values('access_level','user__username','user__department','user__job_role','user__id')[offset:offset+limit]
        list_of_dtos = []
        for user_obj in userobjects:
            list_of_dtos.append(
                userdto(
                id=user_obj['user__id'],
                person_name=user_obj['user__username'],
                department=user_obj['user__department'],
                job_role=user_obj['user__job_role'],
                access_level=user_obj['access_level']
                ))
        user_dto = UserDto(
            count=count,
            users=list_of_dtos
            )
        return user_dto

    # def get_requests(self) -> List[RequestsDto]:

    #     # queryset = Item.objects.prefetch_related('resource__name','user','access_level')
    #     # requests = Request.objects.prefetch_related(Prefetch('item',queryset=queryset)).\
    #     #             values_list('item__user__username',
    #     #                         'item__name',
    #     #                         'item__useraccess__access_level',
    #     #                         'item__resource__name',
    #     #                         'duration',
    #     #                         'id',
    #     #                         'item__resource__image_url'
    #     #                         )
    #     requests = Request.objects.all().\
    #                 values_list('item__user__username',
    #                             'item__name',
    #                             'item__useraccess__access_level',
    #                             'item__resource__name',
    #                             'duration',
    #                             'id',
    #                             'item__resource__image_url'
    #                             )


    #     list_of_requests = []
    #     for request in requests:
    #         list_of_requests.append(
    #             RequestsDto(
    #                 id = request[5],
    #                 name=request[0],
    #                 access_level=request[2],
    #                 duedatetime=request[4],
    #                 resource_name=request[3],
    #                 item_name=request[1],
    #                 url=request[6]
    #                 )
    #             )
    #     return list_of_requests
    def get_requests(self) -> List[RequestsDto]:

        queryset = Item.objects.prefetch_related('user','access_level')
        requests = Request.objects.prefetch_related('user','resource',Prefetch('item',queryset=queryset)).\
                    values('user__username',
                                'item__name',
                                'item__useraccess__access_level'
                                'resource__name',
                                'duration',
                                'id',
                                'user__profile_pic'
                                )

        requests = UserAccess.objects.all().values('access_level','item__')
        request_dict = {}
        for request in requests:
            sub_dict = {
                "name": request["user__username"],
                "access_level": request["item__useraccess__access_level"],
                "duedatetime": request["duedatetime"],
                "resource_name": request["resource__name"],
                "item_name": request["item__name"],
                "url": request["user__profile_pic"]
            }
            request_dict[request["id"]] = sub_dict


        list_of_requests = []

        for key,request in request_dict.items():
            list_of_requests.append(
                RequestsDto(
                    id = key,
                    name=request["name"],
                    access_level=request["access_level"],
                    duedatetime=request["duedatetime"],
                    resource_name=request["resource_name"],
                    item_name=request["item__name"],
                    url=request["url"]
                    )
                )
        return list_of_requests

    def check_for_valid_input(self, list_ids: List[int]):
        for id in list_ids:
            if id <= 0 :
                return False
        return True
