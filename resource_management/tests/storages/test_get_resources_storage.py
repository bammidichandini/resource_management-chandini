import pytest
from resource_management.storages.resources_storage import StorageImplementation


@pytest.mark.django_db
def test_get_resources(resource_dto, create_resources):

    #arrange

    expected_dto_list = resource_dto
    storage = StorageImplementation()

    #act
    resources_list = storage.get_resources()

    #assert
    assert expected_dto_list[0].name == resources_list[0].name