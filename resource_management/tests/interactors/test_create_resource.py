import pytest
from unittest.mock import create_autospec, patch
from resource_management.exceptions.exceptions import UserCannotManipulateException
from resource_management.interactors.storages.resources_storage_interface import StorageInterface
from resource_management.interactors.presenters.presenter_interface import PresenterInterface
from resource_management.interactors.create_resources_interactor import CreateResourceInteractor
# from user_auth.interfaces.service_interface import ServiceInterface


@pytest.mark.django_db()
@patch('resource_management.adapters.auth_service.AuthService.get_user_dtos')
def test_create_resource(get_user_dtos, user_dtos, resource_dtos):

    #arrange
    user_id = 1

    get_user_dtos.return_value = user_dtos
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)


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
    # storage.is_admin.assert_called_once_with(user_id)


@pytest.mark.django_db()
@patch('resource_management.adapters.auth_service.AuthService.get_user_dtos')
def test_create_resource_with_user(get_user_dtos, user_dtos1, resource_dtos):

    #arrange
    user_id = 1

    get_user_dtos.return_value = user_dtos1
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    presenter.raise_user_cannot_manipulate_exception.side_effect = \
        UserCannotManipulateException

    interactor = CreateResourceInteractor(
        storage=storage,
        presenter=presenter
        )

    #act
    with pytest.raises(UserCannotManipulateException):
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
