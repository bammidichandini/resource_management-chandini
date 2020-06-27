import pytest
from resource_management.models import Request
from resource_management.storages.requests_storage_implementation import StorageImplementation
from resource_management.exceptions.exceptions import InvalidIdException


# @pytest.mark.parametrize("request_ids_list", [
#     ([1,0]),([-1,2])])
# @pytest.mark.django_db
# def test_set_status(request_ids_list):

#     # arrange

#     status = "Accepted"
#     reason = "something"

#     storage = StorageImplementation()

#     # act
#     with pytest.raises(InvalidIdException):
#         storage.set_status(
#             request_ids_list=request_ids_list,
#             reason=reason,
#             status=status
#             )

@pytest.mark.django_db
def test_set_status_with_valid_details(create_requests):

    # arrange

    status = "Accepted"
    reason = "something"
    request_ids_list = [1]

    storage = StorageImplementation()

    # act

    storage.set_status(
        request_ids_list=request_ids_list,
        status=status,
        reason=reason,
        )

    # assert
    request = Request.objects.get(id=1)
    assert request.status == status


@pytest.mark.django_db
def test_set_status_with_valid_details_reject(create_requests):

    # arrange

    status = "Rejected"
    reason = "something"
    request_ids_list = [1]

    storage = StorageImplementation()

    # act

    storage.set_status(
        request_ids_list=request_ids_list,
        status=status,
        reason=reason,
        )

    # assert
    request = Request.objects.get(id=1)
    assert request.status == status
