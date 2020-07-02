import pytest
from resource_management.models import Resource
from resource_management.storages.resources_storage import StorageImplementation


@pytest.mark.django_db
def test_create_resource_storage(resource_dtos):

    #arrange
    user_id = 1


    storage = StorageImplementation()

    #act
    storage.create_resource(
        resource_dto=resource_dtos,
        user_id=user_id
        )

    #assert
    Resource.objects.filter(
        image_url=resource_dtos.image_url,
        name=resource_dtos.name,
        item_name=resource_dtos.item_name,
        link=resource_dtos.link,
        description=resource_dtos.description
        ).exists()
