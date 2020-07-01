import pytest
from unittest.mock import create_autospec, patch
from resource_management.exceptions.exceptions import (
    UserCannotManipulateException,
    InvalidIdException
    )
from django_swagger_utils.drf_server.exceptions import Forbidden, NotFound
from resource_management.interactors.storages.resources_storage_interface import StorageInterface
from resource_management.interactors.presenters.presenter_interface import PresenterInterface
from resource_management.interactors.update_resource_interactor import UpdateResourceInteractor


@pytest.mark.django_db
@patch('resource_management.adapters.auth_service.AuthService.get_user_dtos')
def test_update_resource(
    get_user_dtos, user_dtos, resource_dtos):

    #arrange
    resource_id = 1
    user_id = 1

    get_user_dtos.return_value = user_dtos

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    storage.get_resource_ids.return_value = [1,2]
    interactor = UpdateResourceInteractor(
        storage=storage,
        presenter=presenter
        )

    #act
    interactor.update_resource_interactor(
            resource_id=resource_id,
            user_id=user_id,
            resource_dto=resource_dtos
        )

    #assert
    storage.update_resource.assert_called_once_with(
        resource_id=resource_id,
        user_id=user_id,
        resource_dto=resource_dtos
        )


@pytest.mark.django_db
@patch('resource_management.adapters.auth_service.AuthService.get_user_dtos')
def test_update_resource_with_user(get_user_dtos, user_dtos1, resource_dtos):

    #arrange
    resource_id = 1
    user_id = 1

    get_user_dtos.return_value = user_dtos1

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    storage.get_resource_ids.return_value = [1,2]
    presenter.raise_user_cannot_manipulate_exception.side_effect = \
       Forbidden


    interactor = UpdateResourceInteractor(
        storage=storage,
        presenter=presenter
        )

    #act
    with pytest.raises(Forbidden):
        interactor.update_resource_interactor(
            resource_id=resource_id,
            user_id=user_id,
            resource_dto=resource_dtos
            )

@pytest.mark.parametrize("resource_id", [
    ((30),(20))
])
@patch('resource_management.adapters.auth_service.AuthService.get_user_dtos')
def test_update_resource_with_user_invalid_data(
    get_user_dtos, user_dtos, resource_dtos, resource_id):

    #arrange
    user_id = 1

    get_user_dtos.return_value = user_dtos

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    storage.get_resource_ids.return_value = [1,2]
    presenter.raise_invalid_id_exception.side_effect = \
        NotFound


    interactor = UpdateResourceInteractor(
        storage=storage,
        presenter=presenter
        )

    #act
    with pytest.raises(NotFound):
        interactor.update_resource_interactor(
            resource_id=resource_id,
            user_id=user_id,
            resource_dto=resource_dtos
            )
