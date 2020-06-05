import pytest
from resource_management.storages.requests_storage_implementation import StorageImplementation


@pytest.mark.django_db
def test_get_user_requests(
    get_user_requests_dto,
    create_requests,
    create_useraccess,
    create_users1
):

    # assert

    user_id = 1
    expected_response = get_user_requests_dto

    storage = StorageImplementation()

    # act

    response = storage.get_user_requests(user_id=user_id)

    # assert

    assert expected_response[0].resource_name == response[0].resource_name
    assert expected_response[0].item_name == response[0].item_name
    assert expected_response[0].access_level == response[0].access_level
    assert expected_response[0].status == response[0].status