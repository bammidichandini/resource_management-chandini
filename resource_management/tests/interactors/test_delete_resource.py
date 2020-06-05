import pytest
from unittest.mock import create_autospec
from resource_management.exceptions.exceptions import (
    UserCannotManipulateException,
    InvalidIdException
    )
from resource_management.interactors.storages.resources_storage_interface import StorageInterface
from resource_management.interactors.presenters.presenter_interface import PresenterInterface
from resource_management.interactors.delete_resource_interactor import DeleteResourcesInteractor


def test_delete_resource():

    #arrange
    resource_ids_list = [1,2,3]
    user_id = 1

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    storage.is_admin.return_value = True
    storage.check_for_valid_input.return_value = True

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
    storage.is_admin.assert_called_once_with(user_id)
    storage.check_for_valid_input.assert_called_once_with(resource_ids_list)


def test_delete_resource_with_user():

    #arrange
    resource_ids_list = [1,2,3]
    user_id = 1

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    storage.check_for_valid_input.return_value = True
    storage.is_admin.return_value = False
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



@pytest.mark.parametrize("resource_ids_list", [
    ([-1,2,3]),([0,1,2])
])
def test_delete_resource_with_invalid_ids(resource_ids_list):

    #arrange

    user_id = 1

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    storage.check_for_valid_input.return_value = False
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

