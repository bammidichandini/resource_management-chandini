import pytest
from resource_management.models import Request
from resource_management.exceptions.exceptions import InvalidDetailsException
from resource_management.storages.requests_storage_implementation import StorageImplementation


@pytest.mark.django_db
def test_create_user_request(
    add_request_dto,
    create_resources,
    create_useraccess
):

    # arrange
    user_id = 1

    storage = StorageImplementation()

    # act
    storage.create_new_user_request(
        user_id=user_id,
        request_dto=add_request_dto
        )

    # assert
    value = Request.objects.filter(
        duration=add_request_dto.duedatetime
        ).exists()
    assert value == True

