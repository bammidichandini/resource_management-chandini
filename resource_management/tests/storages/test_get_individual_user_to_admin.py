import pytest
from resource_management.models import User
from resource_management.storages.requests_storage_implementation import StorageImplementation


@pytest.mark.django_db
def test_get_individual_user_details(
    create_users1,
    create_useraccess,
    user_requests_dto
):

    # arrange

    expected = user_requests_dto
    user_id = 1
    storage = StorageImplementation()


    # act
    actual = storage.get_individual_user_details_to_admin(
        user_id=user_id
        )


    # assert
    assert actual[0].person_name == expected[0].person_name
    assert actual[0].department == expected[0].department
    assert actual[0].job_role == expected[0].job_role
    assert actual[0].profile_pic == expected[0].profile_pic
    assert actual[0].resource_name == expected[0].resource_name
    assert actual[0].item_name == expected[0].item_name
    assert actual[0].access_level == expected[0].access_level
    assert actual[0].description == expected[0].description
    assert actual[0].link == expected[0].link

