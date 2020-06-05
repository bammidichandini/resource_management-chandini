import pytest
from resource_management.storages.user_details_to_admin_storages import StorageImplementation


@pytest.mark.django_db
def test_get_user_details_to_admin(
    create_users1,
    user_details
):

    # arrange

    expected_response = user_details
    storage = StorageImplementation()

    # act
    actual_response = storage.get_user_details_to_admin()

    # assert
    assert expected_response[0].person_name == actual_response[0].person_name
    assert expected_response[0].department == actual_response[0].department
    assert expected_response[0].job_role == actual_response[0].job_role
    assert expected_response[0].url == actual_response[0].url
