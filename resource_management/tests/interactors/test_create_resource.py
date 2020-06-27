import pytest
from unittest.mock import create_autospec
#from resource_management.exceptions.exceptions import UserCannotManipulateException
from django_swagger_utils.drf_server.exceptions import Forbidden
from resource_management.interactors.storages.resources_storage_interface import StorageInterface
from resource_management.interactors.presenters.presenter_interface import PresenterInterface
from resource_management.interactors.create_resources_interactor import CreateResourceInteractor


@pytest.mark.django_db()
def test_create_resource(resource_dtos):

    #arrange
    user_id = 1

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    storage.is_admin.return_value = True

    interactor = CreateResourceInteractor(
        storage=storage,
        presenter=presenter
        )

    #act
    interactor.create_resource_interactor(
        resource_dtos,
        user_id=user_id
        )

    #assert
    storage.create_resource.assert_called_once_with(
        resource_dtos,
        user_id=user_id
        )
    storage.is_admin.assert_called_once_with(user_id)


def test_create_resource_with_user(resource_dtos):

    #arrange
    user_id = 1

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    storage.is_admin.return_value =False
    presenter.raise_user_cannot_manipulate_exception.side_effect = \
        Forbidden

    interactor = CreateResourceInteractor(
        storage=storage,
        presenter=presenter
        )

    #act
    with pytest.raises(Forbidden):
        interactor.create_resource_interactor(
            resource_dtos,
            user_id=user_id
            )

    # #assert
    # storage.create_resource.assert_called_once_with(
    #     resource_dtos,
    #     user_id=user_id
    #     )
    # presenter.raise_user_cannot_manipulate_exception.assert_called_once()
