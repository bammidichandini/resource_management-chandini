from abc import ABC
from abc import abstractmethod
from typing import List
from resource_management.dtos.dtos import(
     ItemDto,
     UserDto,
     RequestsDto,
     ResourceItemDto,
     ResourceItemParametersDto
     )
from resource_management.models import (
    Resource,
    User,
    Item
    )
from resource_management.models.item import (
    UserAccess
    )
from django.db.models import Prefetch
from resource_management.interactors.storages.item_storages import \
    StorageInterface
from resource_management.exceptions.exceptions import UserCannotManipulateException



class StorageImplementation(StorageInterface):

    def create_item(
        self,
        item_dto: ItemDto,
        user_id: int
        ):
        is_admin = self.is_admin_or_user(user_id=user_id)
        resource = Resource.objects.get(name=item_dto.resource_name)
        if is_admin:
            access_level=item_dto.access_level
            user = User.objects.get(id=user_id)
            item = Item.objects.create(
                name=item_dto.item_name,
                link=item_dto.link,
                resource=resource,
                description=item_dto.description,
                )
            UserAccess.objects.create(
                access_level=access_level,
                item_name=item.id,
                user=user
            )
        else:
            raise UserCannotManipulateException



    def delete_item_interactor(self,
                               item_ids_list: List[int],
                               user_id: int
                               ):
        is_admin = self.is_admin_or_user(user_id=user_id)

        if is_admin:
            Item.objects.filter(id__in=item_ids_list).delete()

        else:
            raise UserCannotManipulateException

    @staticmethod
    def is_admin_or_user(user_id):
        is_admin = User.objects.get(id=user_id).is_admin
        return is_admin


    def update_item_interactor(self,
                               item_id: int,
                               item_dto: ItemDto,
                               user_id: int,
                               resource_name: str
                               ):
        is_admin = self.is_admin_or_user(user_id=user_id)
        resource = Resource.objects.get(name=item_dto.resource_name)
        if is_admin:
            Item.objects.filter(
                id=item_id
                ).update(
                    name=item_dto.item_name,
                    link=item_dto.link,
                    resource=resource,
                    description=item_dto.description,
                    access_level=item_dto.access_level
                    )
        else:
            raise UserCannotManipulateException


    # def is_admin(self, user_id: int) -> List[int]:
    #     is_admin = User.objects.get(id=user_id).is_admin
    #     return is_admin


    def get_resource_items(self, req_param_dto : ResourceItemParametersDto)\
                    -> List[ResourceItemDto]:
        resource_id = req_param_dto.resource_id
        offset = req_param_dto.offset
        limit = req_param_dto.limit
        item_objs = Item.objects.filter(resource_id=resource_id)
        item_dto_list = self.convert_and_get_item_dto_objs_list(
            item_objs=item_objs,
            offset=offset,
            limit=limit
            )
        return item_dto_list

    @staticmethod
    def convert_and_get_item_dto_objs_list(
        item_objs,
        offset,
        limit
        ):
        item_dto_list = []
        Item.objects.all()
        for item_obj in item_objs:
            item_dto_list.append(
                ResourceItemDto(
                item_name=item_obj.name,
                link=item_obj.link,
                description=item_obj.description
                )
                )
        items_list_dto = []
        for offset in range(limit):
            items_list_dto.append(item_dto_list[offset])
        return items_list_dto


    def get_users_for_items(self, item_id: int) -> List[UserDto]:
        # access_objs = Accesslevel.objects.prefetch_related(Prefetch('user',User.objects.filter(item__id=item_id).prefetch_related('item'))).exclude(access_level__isnull=True)
        item = Item.objects.get(id=item_id)
        userobjects = UserAccess.objects.prefetch_related('user').filter(item_id=item.id).\
            values_list('access_level','user__username','user__department','user__job_role')
        list_of_dtos = []
        for user_obj in userobjects:
            list_of_dtos.append(
                UserDto(
                person_name=user_obj[1],
                department=user_obj[2],
                job_role=user_obj[3],
                access_level=user_obj[0]
                ))
        return list_of_dtos

    def get_requests(self) -> List[RequestsDto]:

        queryset = Item.objects.prefetch_related('resource__name')
        requests = UserAccess.objects.prefetch_related(Prefetch('item',queryset=queryset)).\
                    values_list('user__username',
                                'item__name',
                                'access_level',
                                'item__resource__name',
                                'duration'
                                )

        list_of_requests = []
        for request in requests:
            list_of_requests.append(
                RequestsDto(
                    name=request[0],
                    access_level=request[2],
                    duedatetime=request[4],
                    resource_name=request[3],
                    item_name=request[1]
                    )
                )
        return list_of_requests