import pytest
from resource_management.storages.resources_storage import StorageImplementation



@pytest.mark.django_db()
def test_delete_resource(create_resources):

    #arrange
    user_id = 1

    resources_list = [1]
    storage = StorageImplementation()

    #act
    storage.delete_resources(
        resource_ids_list=resources_list,
        user_id=user_id
        )


