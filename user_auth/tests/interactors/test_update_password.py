import pytest
from unittest.mock import create_autospec
from user_auth.models import User
from user_auth.interactors.storages.user_profile_storage_interface import StorageInterface
from user_auth.interactors.presenters.presenter_interface import PresenterInterface
from user_auth.interactors.update_password_interactor import UpdatePasswordInteractor


@pytest.mark.django_db
def test_update_password(create_users1):

    # arrange

    user_id = 1
    password="hello"
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    interactor = UpdatePasswordInteractor(
        storage=storage,
        presenter=presenter
        )

    # act
    interactor.update_password_interactor(
        user_id=user_id,
        password=password
        )


    # assert
    storage.update_password.assert_called_once_with(
        user_id=user_id,
        password=password
     )
    # user = User.objects.get(id=1)
    # assert user.check_password(password) == True
