import pytest
from unittest.mock import create_autospec, patch
from resource_management.exceptions.exceptions import(
    UserCannotManipulateException,
    InvalidIdException
    )
from django_swagger_utils.drf_server.exceptions import Forbidden, NotFound
from resource_management.interactors.update_item_interactor import UpdateItemInteractor
from resource_management.interactors.storages.item_storages import StorageInterface
from resource_management.interactors.presenters.presenter_interface import PresenterInterface


@pytest.mark.django_db
@patch('resource_management.adapters.auth_service.AuthService.get_user_dtos')
def test_update_item(
    get_user_dtos,
    user_dtos,
    item_dto
    ):

    # arrange

    item_id = 1
    user_id = 1
    expected_dto =  item_dto

    get_user_dtos.return_value = user_dtos

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    # storage.check_for_valid_input.return_value = True
    # storage.is_admin.return_value = True
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


@pytest.mark.django_db
@patch('resource_management.adapters.auth_service.AuthService.get_user_dtos')
def test_update_item_with_user_raises_exception(
    get_user_dtos,
    user_dtos1,
    item_dto
    ):

    # arrange

    item_id = 1
    user_id = 1

    get_user_dtos.return_value = user_dtos1

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    storage.get_item_ids.return_value = [1,2]
    # storage.check_for_valid_input.return_value = True
    # storage.is_admin.return_value = False
    presenter.raise_user_cannot_manipulate_exception.side_effect = \
        Forbidden

    interactor = UpdateItemInteractor(
        storage=storage,
        presenter=presenter
        )

    # act
    with pytest.raises(Forbidden):
        interactor.update_item_interactor(
            user_id=user_id,
            item_id=item_id,
            item_dto=item_dto
            )

@pytest.mark.parametrize("item_id", [
    (100),(30)
])
@patch('resource_management.adapters.auth_service.AuthService.get_user_dtos')
def test_update_item_with_invalid_input(get_user_dtos, user_dtos, item_id, item_dto):
    # arrange


    user_id = 1

    get_user_dtos.return_value = user_dtos

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    storage.get_item_ids.return_value = [1,2]

    presenter.raise_invalid_id_exception.side_effect = \
        NotFound

    interactor = UpdateItemInteractor(
        storage=storage,
        presenter=presenter
        )

    # act
    with pytest.raises(NotFound):
        interactor.update_item_interactor(
            user_id=user_id,
            item_id=item_id,
            item_dto=item_dto
            )
