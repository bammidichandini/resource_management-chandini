import pytest
from unittest.mock import create_autospec
from resource_management.exceptions.exceptions import (
    UserCannotManipulateException,
    InvalidIdException
    )
from resource_management.interactors.storages.resources_storage_interface import StorageInterface
from resource_management.interactors.presenters.presenter_interface import PresenterInterface
from resource_management.interactors.update_resource_interactor import UpdateResourceInteractor


@pytest.mark.django_db()
def test_update_resource(resource_dtos):

    #arrange
    resource_id = 1
    user_id = 1

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    storage.is_admin.return_value = True
    storage.check_for_valid_input.return_value = True

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


@pytest.mark.django_db()
def test_update_resource_with_user(resource_dtos):

    #arrange
    resource_id = 1
    user_id = 1


    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    storage.is_admin.return_value = False
    storage.check_for_valid_input.return_value = True
    presenter.raise_user_cannot_manipulate_exception.side_effect = \
        UserCannotManipulateException


    interactor = UpdateResourceInteractor(
        storage=storage,
        presenter=presenter
        )

    #act
    with pytest.raises(UserCannotManipulateException):
        interactor.update_resource_interactor(
            resource_id=resource_id,
            user_id=user_id,
            resource_dto=resource_dtos
            )

@pytest.mark.parametrize("resource_id", [
    ((1),(0))
])
@pytest.mark.django_db()
def test_update_resource_with_user_invalid_data(resource_dtos, resource_id):

    #arrange
    resource_id = 1
    user_id = 1


    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    storage.check_for_valid_input.return_value = False
    presenter.raise_invalid_id_exception.side_effect = \
        InvalidIdException


    interactor = UpdateResourceInteractor(
        storage=storage,
        presenter=presenter
        )

    #act
    with pytest.raises(InvalidIdException):
        interactor.update_resource_interactor(
            resource_id=resource_id,
            user_id=user_id,
            resource_dto=resource_dtos
            )

