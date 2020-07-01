import pytest
from unittest.mock import create_autospec, patch
from resource_management.exceptions.exceptions import (
    UserCannotManipulateException,
    InvalidIdException
    )
from django.core.exceptions import ObjectDoesNotExist
from resource_management.exceptions.exceptions import InvalidIdException
from django_swagger_utils.drf_server.exceptions import NotFound
from resource_management.interactors.delete_items_interactor import DeleteItemsInteractor
from resource_management.interactors.storages.item_storages import StorageInterface
from resource_management.interactors.presenters.presenter_interface import PresenterInterface


@pytest.mark.django_db
@patch('resource_management.adapters.auth_service.AuthService.get_user_dtos')
def test_delete_items(get_user_dtos, user_dtos):

    # arrange

    user_id = 1
    item_ids = [1,2,3]

    get_user_dtos.return_value = user_dtos
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    # storage.check_for_valid_input.return_value = True

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
    # storage.is_admin.assert_called_once_with(user_id)
    # storage.check_for_valid_input.assert_called_once_with(item_ids)


@pytest.mark.django_db
@patch('resource_management.adapters.auth_service.AuthService.get_user_dtos')
def test_delete_items_with_invalid_input(get_user_dtos, user_dtos):

    # arrange

    user_id = 1
    item_ids = [100]

    get_user_dtos.return_value = user_dtos
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

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


@pytest.mark.django_db
@pytest.mark.parametrize("item_ids", [
    ([9,2,3])
])
@patch('resource_management.adapters.auth_service.AuthService.get_user_dtos')
def test_delete_items_with_invalid_item_ids( get_user_dtos, item_ids, user_dtos):

    # arrange

    user_id = 1

    get_user_dtos.return_value = user_dtos
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    presenter.raise_invalid_id_exception.side_effect = NotFound

    interactor = DeleteItemsInteractor(
        storage=storage,
        presenter=presenter
        )

    # act
    with pytest.raises(NotFound):
        interactor.delete_items_interactor(
            user_id=user_id,
            item_ids_list=item_ids
            )


@pytest.mark.django_db
@patch('resource_management.adapters.auth_service.AuthService.get_user_dtos')
def test_delete_items_with_user_raises_exception(get_user_dtos, user_dtos1):

    # arrange

    user_id = 1
    item_ids = [1,2,3]

    get_user_dtos.return_value = user_dtos1
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

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
