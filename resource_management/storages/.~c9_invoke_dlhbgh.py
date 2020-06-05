from abc import ABC
from abc import abstractmethod
from typing import List
from resource_management.dtos.dtos import ItemDto
from resource_management.models import Resource, User
from resource_management.interactors.storages.item_storages import \
    StorageInterface
from resource_management.exceptions.exceptions import UserCannotManipulateException



class StorageInterface(ABC):

    def create_item(
        self,
        item_dto: ItemDto,
        user_id: int
        ):
        is_admin = self.is_admin_or_user(user_id=user_id)
        resource = Resource.objects.get(name=item_dto.resource_name)
        if is_admin:
            Item.objects.create(
                item_name=item_dto.item_name,
                link=item_dto.link,
                resource=resource,
                description=item_dto.description,
                access_level=item_dto.access_level
                )
        else:
            raise UserCannotManipulateException


    @abstractmethod
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


    @abstractmethod
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
                    item_name=item_dto.item_name,
                    link=item_dto.link,
                    resource=resource,
                    description=item_dto.description,
                    access_level=item_dto.access_level
                    )
        else:
            raise UserCannotManipulateException


    @abstractmethod
    def is_admin(self, user_id: int) -> List[int]:
        is_admin = User.objects.get(id=user_id).is_admin
        return is_admin

    @abstractmethod
    def get_resource_items(self, resource_id: int) -> List[ItemDto]:
        item_objs = Item.objects.all(resource_id=resource_id)
        item_dto_list = self.convert_and_get_item_dto_objs_list(
            item_objs=item_objs
            )
        return item_dto_list

    @staticmethod
    def convert_and_get_item_dto_objs_list(item_objs):
        item_dto_list = []

        for item_obj in item_objs:

            item_dto_list.append(
                ItemDto(
                item_name=item_obj.item_name,
                resource_name=item_obj.resource.name,
                link=item_obj.link,
                description=item_obj.description,
                access_level=item_obj.access_level
                )
                )

        return item_dto_list


    # @abstractmethod
    # def get_user_items(self, user_id: int) -> List[ItemDto]:
    #     pass