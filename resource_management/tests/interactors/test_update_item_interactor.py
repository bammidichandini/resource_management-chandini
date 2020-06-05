import pytest
from unittest.mock import create_autospec
from resource_management.exceptions.exceptions import(
    UserCannotManipulateException,
    InvalidIdException
    )
from resource_management.interactors.update_item_interactor import UpdateItemInteractor
from resource_management.interactors.storages.item_storages import StorageInterface
from resource_management.interactors.presenters.presenter_interface import PresenterInterface


@pytest.mark.django_db
def test_update_item(
    item_dto
    ):

    # arrange

    item_id = 1
    user_id = 1
    expected_dto =  item_dto

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    storage.check_for_valid_input.return_value = True
    storage.is_admin.return_value = True
    interactor = UpdateItemInteractor(
        storage=storage,
        presenter=presenter
        )

    # act
    interactor.update_item_interactor(
        user_id=user_id,
        item_id=item_id,
        item_dto=item_dto
        )

    # assert
    storage.update_item.assert_called_once_with(
        item_dto=expected_dto,
        user_id=user_id,
        item_id=item_id
        )
    storage.check_for_valid_input.assert_called_once_with([item_id])
    storage.is_admin.assert_called_once_with(user_id)


@pytest.mark.django_db
def test_update_item_with_user_raises_execption(
    item_dto
    ):

    # arrange

    item_id = 1
    user_id = 1


    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    storage.check_for_valid_input.return_value = True
    storage.is_admin.return_value = False
    presenter.raise_user_cannot_manipulate_exception.side_effect = \
        UserCannotManipulateException

    interactor = UpdateItemInteractor(
        storage=storage,
        presenter=presenter
        )

    # act
    with pytest.raises(UserCannotManipulateException):
        interactor.update_item_interactor(
            user_id=user_id,
            item_id=item_id,
            item_dto=item_dto
            )

@pytest.mark.parametrize("item_id", [
    (1),(0)
])
def test_update_item_with_invalid_input(item_id, item_dto):
    # arrange


    user_id = 1


    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    storage.check_for_valid_input.return_value = False
    presenter.raise_invalid_id_exception.side_effect = \
        InvalidIdException

    interactor = UpdateItemInteractor(
        storage=storage,
        presenter=presenter
        )

    # act
    with pytest.raises(InvalidIdException):
        interactor.update_item_interactor(
            user_id=user_id,
            item_id=item_id,
            item_dto=item_dto
            )
