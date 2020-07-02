import pytest
from unittest.mock import create_autospec
from user_auth.models import User
from user_auth.interactors.storages.user_profile_storage_interface \
        import StorageInterface
from user_auth.interactors.presenters.presenter_interface \
        import PresenterInterface
from user_auth.interactors.update_user_profile_interactor \
        import UpdateUserProfileInteractor
from user_auth.constants.enums import Gender


@pytest.mark.django_db
def test_update_user_profile(update_user_profile):

    #  arrange

    user_id = 1
    expected_dto = update_user_profile
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    interactor = UpdateUserProfileInteractor(
        storage=storage,
        presenter=presenter
        )

    #act
    interactor.update_user_details_interactor(
           user_profile_dto=expected_dto,
           user_id=user_id
        )

    #assert
    storage.update_user_details.assert_called_once_with(
            user_profile_dto=expected_dto,
            user_id=user_id
        )


