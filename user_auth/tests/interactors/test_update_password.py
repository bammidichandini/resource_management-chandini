import pytest
from unittest.mock import create_autospec
from resource_management.models import User
from resource_management.interactors.storages.user_profile_storage_interface import StorageInterface
from resource_management.interactors.presenters.presenter_interface import PresenterInterface
from resource_management.interactors.update_password_interactor import UpdatePasswordInteractor


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
    user = User.objects.get(id=1)
    assert user.password == password



