import pytest
from resource_management.models import Request
from resource_management.storages.requests_storage_implementation import StorageImplementation
from resource_management.exceptions.exceptions import (
    InvalidIdException,
    InvalidDetailsException
    )

# @pytest.mark.parametrize("request_id", [
#     (-1),(0)])
# @pytest.mark.django_db
# def test_update_user_request_with_invalid_id(
#     request_update_dto,
#     request_id,
#     create_useraccess
# ):

#     # arrange

#     user_id = 1
#     storage = StorageImplementation()

#     # act
#     with pytest.raises(InvalidIdException):
#         storage.update_user_request(
#             user_id=user_id,
#             update_dto=request_update_dto,
#             request_id=request_id
#             )

@pytest.mark.django_db
def test_update_user_request(
    request_update_dto,
    create_useraccess,
    create_requests
):

    # arrange

    user_id = 1
    request_id = 1
    storage = StorageImplementation()

    # act
    storage.update_user_request(
            user_id=user_id,
            update_dto=request_update_dto,
            request_id=request_id
            )

    # assert
    request =  Request.objects.get(id=1)
    item = request.item
    resource = item.resource
    assert resource.name == request_update_dto.resource_name
    assert item.name == request_update_dto.item_name
    assert request.duration == request_update_dto.duedatetime
    assert request.reason == request_update_dto.access_reason
