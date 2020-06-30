import pytest
from unittest.mock import create_autospec, patch
from resource_management.exceptions.exceptions import (
    UserCannotManipulateException,
    InvalidIdException
    )
from resource_management.interactors.storages.resources_storage_interface import StorageInterface
from resource_management.interactors.presenters.presenter_interface import PresenterInterface
from resource_management.interactors.delete_resource_interactor import DeleteResourcesInteractor


@pytest.mark.django_db
@patch('resource_management.adapters.auth_service.AuthService.get_user_dtos')
def test_delete_resource(get_user_dtos, user_dtos):

    #arrange
    resource_ids_list = [1,2,3]
    user_id = 1

    get_user_dtos.return_value = user_dtos
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    interactor = DeleteResourcesInteractor(
        storage=storage,
        presenter=presenter
        )

    #act
    interactor.delete_resources_interactor(
        user_id=user_id,
        resource_ids_list=resource_ids_list
        )

    #assert
    storage.delete_resources.assert_called_once_with(
       user_id=user_id,
       resource_ids_list=resource_ids_list
        )


@pytest.mark.django_db
@patch('resource_management.adapters.auth_service.AuthService.get_user_dtos')
def test_delete_resource_with_user(get_user_dtos, user_dtos1):

    #arrange
    resource_ids_list = [1,2,3]
    user_id = 1

    get_user_dtos.return_value = user_dtos1
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    presenter.raise_user_cannot_manipulate_exception.side_effect = \
        UserCannotManipulateException


    interactor = DeleteResourcesInteractor(
        storage=storage,
        presenter=presenter
        )

    #act
    with pytest.raises(UserCannotManipulateException):
        interactor.delete_resources_interactor(
            user_id=user_id,
            resource_ids_list=resource_ids_list
            )



@pytest.mark.django_db
@pytest.mark.parametrize("resource_ids_list", [
    ([20,2,3]),([100,1,2])
])
@patch('resource_management.adapters.auth_service.AuthService.get_user_dtos')
def test_delete_resource_with_invalid_ids(get_user_dtos, resource_ids_list, user_dtos1):

    #arrange

    user_id = 1

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    get_user_dtos.return_value = user_dtos1
    presenter.raise_invalid_id_exception.side_effect = InvalidIdException


    interactor = DeleteResourcesInteractor(
        storage=storage,
        presenter=presenter
        )

    #act
    with pytest.raises(InvalidIdException):
        interactor.delete_resources_interactor(
            user_id=user_id,
            resource_ids_list=resource_ids_list
            )
