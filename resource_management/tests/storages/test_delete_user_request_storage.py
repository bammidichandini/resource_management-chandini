import pytest
from resource_management.models import Request
from resource_management.storages.requests_storage_implementation import StorageImplementation
from resource_management.exceptions.exceptions import (
    InvalidIdException
    )


# @pytest.mark.parametrize("request_id", [
#     (-1),(0)])
# @pytest.mark.django_db
# def test_delete_user_request_with_invalid_id_raises_exception(request_id):

#     # arrange

#     user_id = 1
#     storage = StorageImplementation()

#     # act
#     with pytest.raises(InvalidIdException):
#         storage.delete_user_request(
#             request_id=request_id,
#             user_id=user_id
#             )

@pytest.mark.django_db
def test_delete_user_request(
    create_requests,
    create_useraccess
):

    # arrange

    user_id = 1
    request_id = 1
    storage = StorageImplementation()

    # act
    storage.delete_user_request(
        request_id=request_id,
        user_id=user_id
        )

    # assert
    value = Request.objects.filter(id=request_id).exists()
    assert value == False
