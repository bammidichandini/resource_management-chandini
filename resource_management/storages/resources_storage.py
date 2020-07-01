from typing import List
from resource_management.models import Resource, Item, UserAccess, Request
from resource_management.dtos.dtos import ResourceDto, ItemDto, Itemdto, itemdto
from django.core.exceptions import ObjectDoesNotExist
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
        Resource.objects.create(
            image_url=resource_dto.image_url,
            name=resource_dto.name,
            item_name=resource_dto.item_name,
            link=resource_dto.link,
            description=resource_dto.description
            )


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
       resources =  Resource.objects.filter(
            id=resource_id
            )
       resources.update(
                image_url=resource_dto.image_url,
                name=resource_dto.name,
                item_name=resource_dto.item_name,
                link=resource_dto.link,
                description=resource_dto.description
                )


    def delete_resources(self,
                         user_id: int,
                         resource_ids_list: List[int]):

        resources = Resource.objects.filter(id__in=resource_ids_list)
        resources.delete()

    def get_resource_ids(self):
        resources = Resource.objects.values_list('id', flat=True)
        return resources

    def get_user_resources(self, user_id: int) -> List[itemdto]:

        requests = Request.objects.filter(user_id=user_id).prefetch_related('item', 'resource')

        items_list = []
        for request in requests:
            items_list.append(itemdto(
                id=request.item.id,
                item_name=request.item.name,
                link=request.item.link,
                resource=request.resource.name
                ))
        return items_list

