import pytest
from resource_management.storages.item_storages_implementation import StorageImplementation


@pytest.mark.django_db
def test_get_resources_item(item_dto,
                            create_items,
                            get_req_param
                            ):

    # arrange


    expected_dto_list = item_dto
    storage = StorageImplementation()

    # act
    items_list = storage.get_resource_items(get_req_param)

    # assert
    assert expected_dto_list == items_list
