from typing import List
from resource_management.models import Resource, User, Item, UserAccess
from resource_management.dtos.dtos import ResourceDto, ItemDto
from django.db.models import Prefetch
from resource_management.interactors.storages.resources_storage_interface import \
    StorageInterface
from resource_management.exceptions.exceptions import (
    UserCannotManipulateException,
    InvalidDetailsException
    )


class StorageImplementation(StorageInterface):

    def create_resource(self,
                        resource_dto: ResourceDto,
                        user_id: int
                        ):
        is_admin = self.is_admin_or_user(user_id=user_id)


        if is_admin:
            Resource.objects.create(
                image_url=resource_dto.image_url,
                name=resource_dto.name,
                item_name=resource_dto.item_name,
                link=resource_dto.link,
                description=resource_dto.description
                )
        else:
            raise UserCannotManipulateException


    def get_resources(self) -> List[ResourceDto]:
        resource_objs = Resource.objects.all()
        resource_dto_list = self.convert_and_get_resource_dto_objs_list(
            resource_objs=resource_objs
            )
        return resource_dto_list

    @staticmethod
    def convert_and_get_resource_dto_objs_list(resource_objs):
        resource_dto_list = []

        for resource_obj in resource_objs:
            resource_dto_list.append(
                ResourceDto(
                id=resource_obj.id,
                image_url=resource_obj.image_url,
                name=resource_obj.name,
                item_name=resource_obj.item_name,
                link=resource_obj.link,
                description=resource_obj.description
                )
                )

        return resource_dto_list

    def update_resource(self, resource_id: int,
                        resource_dto: ResourceDto,
                        user_id: int
                        ):
        is_admin = self.is_admin_or_user(user_id=user_id)
        if is_admin:

            Resource.objects.filter(
                id=resource_id
                ).update(
                    image_url=resource_dto.image_url,
                    name=resource_dto.name,
                    item_name=resource_dto.item_name,
                    link=resource_dto.link,
                    description=resource_dto.description
                    )
        else:
            raise UserCannotManipulateException


    def delete_resources(self,
                         user_id: int,
                         resource_ids_list: List[int]):

        is_admin = self.is_admin_or_user(user_id=user_id)

        if is_admin:
            Resource.objects.filter(id__in=resource_ids_list).delete()

        else:
            raise UserCannotManipulateException

    @staticmethod
    def is_admin_or_user(user_id):
        is_admin = User.objects.get(id=user_id).is_admin
        return is_admin


    def get_user_resources(self, user_id: int) -> List[ItemDto]:

        queryset = Item.objects.prefetch_related('resource')
        items = UserAccess.objects.filter(user_id=user_id).\
            prefetch_related(Prefetch('item',queryset=queryset)).\
            values(
                'item__resource__name',
                'item__name',
                'access_level',
                'item__link',
                'item__description'
                )
        items_list = []
        for item in items:
            items_list.append(ItemDto(
                item_name=item["item__name"],
                link=item["item__link"],
                resource_name=item["item__resource__name"],
                description=item["item__description"],
                access_level=item["access_level"]
                ))
        return items_list

    def check_for_valid_input(self, list_ids: List[int]):
        for id in list_ids:
            if id <= 0 :
                return False

    def is_admin(self, user_id: int) -> List[int]:
        is_admin = User.objects.get(id=user_id).is_admin
        return is_admin
