import pytest
from resource_management.storages.item_storages_implementation import StorageImplementation


@pytest.mark.django_db
def test_get_item_users_storage(
    create_users1,
    create_useraccess,
    get_item_users
    ):

    # arrange

    item_id = 1
    expected_response = get_item_users

    storage = StorageImplementation()

    #act
    actual_response = storage.get_users_for_items(item_id)

    #assert
    assert expected_response[0].person_name == actual_response[0].person_name
    assert expected_response[0].department == actual_response[0].department
    assert expected_response[0].job_role == actual_response[0].job_role
    assert expected_response[0].access_level == actual_response[0].access_level
