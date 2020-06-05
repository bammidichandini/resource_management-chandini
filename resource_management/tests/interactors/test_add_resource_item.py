import pytest
from unittest.mock import create_autospec
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
def test_create_resource_item(item_dto):

    #arrange

    user_id = 1

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    storage.is_admin.return_value = True

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
    storage.is_admin.assert_called_once_with(user_id)


def test_create_resource_item_with_user(item_dto):

    #arrange
    user_id = 1

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    storage.is_admin.return_value =False
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

