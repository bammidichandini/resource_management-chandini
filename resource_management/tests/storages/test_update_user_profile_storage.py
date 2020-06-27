import pytest
from resource_management.models import User
from resource_management.exceptions.exceptions import InvalidDetailsException
from resource_management.storages.user_profile_details_storage import StorageImplementation


@pytest.mark.django_db
def test_update_user_profile(create_users,
                             update_user_profile
                            ):

    #arrange

    user_id = 1
    profile_dto = update_user_profile
    storage = StorageImplementation()

    # act
    storage.update_user_details(
        user_id=user_id,
        user_profile_dto=profile_dto
        )

    # assert
    user = User.objects.get(id=1)
    assert user.name == profile_dto.name


