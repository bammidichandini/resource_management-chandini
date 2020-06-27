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
    offset = 0
    limit = 1
    expected_response = get_user_requests_dto

    storage = StorageImplementation()

    # act

    response = storage.get_user_requests(user_id=user_id, offset=offset, limit=limit)

    # assert
    assert expected_response.count == response.count
    assert expected_response.requests[0].resource_name == response.requests[0].resource_name
    assert expected_response.requests[0].item_name == response.requests[0].item_name
    assert expected_response.requests[0].status == response.requests[0].status
