import pytest
from resource_management.storages.item_storages_implementation import StorageImplementation

@pytest.mark.django_db()
def test_delete_items(create_items):

    #arrange
    user_id = 1

    items_list = [1]
    storage = StorageImplementation()

    #act
    storage.delete_items(
         item_ids_list=items_list,
         user_id=user_id
        )


