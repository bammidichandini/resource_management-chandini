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


@pytest.mark.django_db
def test_update_user_profile_with_invalid_name(create_users,
                                               update_profile_with_invalid_name
                                              ):

    #arrange

    user_id = 1
    profile_dto = update_profile_with_invalid_name
    storage = StorageImplementation()

    # act
    with pytest.raises(InvalidDetailsException):
        storage.update_user_details(
            user_id=user_id,
            user_profile_dto=profile_dto
            )



@pytest.mark.django_db
def test_update_user_profile_with_invalid_gmail(create_users,
                                               update_profile_with_invalid_email
                                              ):

    #arrange

    user_id = 1
    profile_dto = update_profile_with_invalid_email
    storage = StorageImplementation()

    # act
    with pytest.raises(InvalidDetailsException):
        storage.update_user_details(
            user_id=user_id,
            user_profile_dto=profile_dto
            )


@pytest.mark.django_db
def test_update_user_profile_with_invalid_gender(create_users,
                                               update_profile_with_invalid_gender
                                              ):

    #arrange

    user_id = 1
    profile_dto = update_profile_with_invalid_gender
    storage = StorageImplementation()

    # act
    with pytest.raises(InvalidDetailsException):
        storage.update_user_details(
            user_id=user_id,
            user_profile_dto=profile_dto
            )
