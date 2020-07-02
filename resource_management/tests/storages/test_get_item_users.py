import pytest
from resource_management.storages.item_storages_implementation import StorageImplementation


@pytest.mark.django_db
def test_get_item_users_storage(
    create_useraccess,
    get_item_users,
    create_requests
    ):

    # arrange

    item_id = 1
    offset = 0
    limit = 1

    expected_response = get_item_users

    storage = StorageImplementation()

    #act
    actual_response = storage.get_users_for_items(
        item_id=item_id,
        offset=offset,
        limit=limit
    )

    #assert
    assert expected_response[0].id == actual_response[0].id
    assert expected_response[0].access_level == actual_response[0].access_level
