import pytest
from unittest.mock import create_autospec, patch
from resource_management.interactors.storages.item_storages \
    import StorageInterface
from resource_management.interactors.presenters.presenter_interface \
    import PresenterInterface
from resource_management.dtos.dtos import ItemDto
from resource_management.interactors.create_resource_item_interactor \
    import CreateResourceItemInteractor
from resource_management.exceptions.exceptions \
    import UserCannotManipulateException


@pytest.mark.django_db
@patch('resource_management.adapters.auth_service.AuthService.get_user_dtos')
def test_create_resource_item(get_user_dtos, user_dtos, item_dto):

    #arrange

    user_id = 1

    get_user_dtos.return_value = user_dtos
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    interactor = CreateResourceItemInteractor(
        storage=storage,
        presenter=presenter
        )

    #act
    interactor.create_item_interactor(item_dto=item_dto,
                           user_id=user_id
                           )

    #assert
    storage.create_item.assert_called_once_with(
        item_dto=item_dto,
        user_id=user_id
        )


@pytest.mark.django_db
@patch('resource_management.adapters.auth_service.AuthService.get_user_dtos')
def test_create_resource_item_with_user(get_user_dtos, user_dtos1, item_dto):

    #arrange
    user_id = 1

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    get_user_dtos.return_value = user_dtos1

    presenter.raise_user_cannot_manipulate_exception.side_effect = \
        UserCannotManipulateException

    interactor = CreateResourceItemInteractor(
        storage=storage,
        presenter=presenter
        )

    #act
    with pytest.raises(UserCannotManipulateException):
        interactor.create_item_interactor(
            item_dto=item_dto,
            user_id=user_id
            )
