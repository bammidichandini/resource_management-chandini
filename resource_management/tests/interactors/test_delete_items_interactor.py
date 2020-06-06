import pytest
from unittest.mock import create_autospec
from resource_management.exceptions.exceptions import (
    UserCannotManipulateException,
    InvalidIdException
    )
from django.core.exceptions import ObjectDoesNotExist
from resource_management.exceptions.exceptions import InvalidIdException
from resource_management.interactors.delete_items_interactor import DeleteItemsInteractor
from resource_management.interactors.storages.item_storages import StorageInterface
from resource_management.interactors.presenters.presenter_interface import PresenterInterface


def test_delete_items():

    # arrange

    user_id = 1
    item_ids = [1,2,3]

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    storage.is_admin.return_value = True
    storage.check_for_valid_input.return_value = True

    interactor = DeleteItemsInteractor(
        storage=storage,
        presenter=presenter
        )

    # act

    interactor.delete_items_interactor(
        user_id=user_id,
        item_ids_list=item_ids
        )

    # assert
    storage.delete_items.assert_called_once_with(
        item_ids_list=item_ids,
        user_id=user_id
        )
    storage.is_admin.assert_called_once_with(user_id)
    storage.check_for_valid_input.assert_called_once_with(item_ids)


def test_delete_items_with_invalid_input():

    # arrange

    user_id = 1
    item_ids = [100]

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    storage.is_admin.return_value = True
    storage.check_for_valid_input.return_value = True
    storage.delete_items.side_effect = ObjectDoesNotExist
    presenter.raise_invalid_id_exception.side_effect = InvalidIdException

    interactor = DeleteItemsInteractor(
        storage=storage,
        presenter=presenter
        )

    # act
    with pytest.raises(InvalidIdException):
        interactor.delete_items_interactor(
            user_id=user_id,
            item_ids_list=item_ids
            )



@pytest.mark.parametrize("item_ids", [
    ([-1,2,3]),([0,1,2])
])
def test_delete_items_with_invalid_item_ids(item_ids):

    # arrange

    user_id = 1

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    storage.check_for_valid_input.return_value = False
    presenter.raise_invalid_id_exception.side_effect = InvalidIdException

    interactor = DeleteItemsInteractor(
        storage=storage,
        presenter=presenter
        )

    # act
    with pytest.raises(InvalidIdException):
        interactor.delete_items_interactor(
            user_id=user_id,
            item_ids_list=item_ids
            )



def test_delete_items_with_user_raises_exception():

    # arrange

    user_id = 1
    item_ids = [1,2,3]

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    storage.check_for_valid_input.return_value = True
    storage.is_admin.return_value = False
    presenter.raise_user_cannot_manipulate_exception.side_effect = \
        UserCannotManipulateException

    interactor = DeleteItemsInteractor(
        storage=storage,
        presenter=presenter
        )

    # act
    with pytest.raises(UserCannotManipulateException):
        interactor.delete_items_interactor(
            user_id=user_id,
            item_ids_list=item_ids
            )

