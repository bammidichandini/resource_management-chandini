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
from resource_management.constants.enums import RequestStatus
from django.core.exceptions import ObjectDoesNotExist
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

        items = Item.objects.filter(id__in=item_ids_list)
        if len(items) == 0:
            raise ObjectDoesNotExist

        items.delete()


    def update_item(
        self,
        item_id: int,
        item_dto: ItemDto,
        user_id: int
        ):
        resource = Resource.objects.get(name=item_dto.resource_name)
        items = Item.objects.filter(
            id=item_id
            )
        if len(items):
            raise ObjectDoesNotExist

        items.update(
                name=item_dto.item_name,
                link=item_dto.link,
                resource=resource,
                description=item_dto.description
                )
        UserAccess.objects.filter(item_id=item_id, user_id=user_id).\
            update(access_level=item_dto.access_level)


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
                id=item_obj.id,
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

        items = Item.objects.filter(id=item_id)
        count = items.count()
        userobjects = items.prefetch_related('user')
        list_of_dtos = []
        for user_obj in userobjects:
            list_of_dtos.append(
                userdto(
                id=user_obj.user.id,
                person_name=user_obj.user.username,
                department=user_obj.user.department,
                job_role=user_obj.user.job_role,
                access_level=user_obj.access_level
                ))
        user_dto = UserDto(
            count=count,
            users=list_of_dtos
            )
        return user_dto


    def get_requests(self) -> List[RequestsDto]:

        requests = Request.objects.filter(status=RequestStatus.Pending.value).prefetch_related('user','item','resource')
        list_of_requests = []

        for request in requests:
            list_of_requests.append(
                RequestsDto(
                    id = request.id,
                    name=request.user.username,
                    access_level=request.access_level,
                    duedatetime=request.duration,
                    resource_name=request.resource.name,
                    item_name=request.item.name,
                    url=request.user.profile_pic
                    )
                )
        return list_of_requests

    def check_for_valid_input(self, list_ids: List[int]):
        for id in list_ids:
            if id <= 0 :
                return False
        return True

    def check_for_valid_offset(self, offset):
        if offset < 0:
            return False
        return True
