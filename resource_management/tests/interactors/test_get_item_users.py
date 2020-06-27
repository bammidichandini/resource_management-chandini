import pytest
from unittest.mock import create_autospec
# from resource_management.exceptions.exceptions import InvalidIdException
from django_swagger_utils.drf_server.exceptions import NotFound
from resource_management.interactors.get_item_accessible_user_interactor \
    import GetUsersForItems
from resource_management.interactors.storages.item_storages import StorageInterface
from resource_management.interactors.presenters.presenter_interface import PresenterInterface


@pytest.mark.django_db
def test_get_item_related_user(get_item_users,
                               get_item_users_response
                               ):

    # arrange

    item_id = 1
    offset = 0
    limit = 1
    expected_response = get_item_users_response

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    storage.check_for_valid_input.return_value = True
    storage.get_users_for_items.return_value = get_item_users
    presenter.get_user_for_items_response.return_value = \
                get_item_users_response

    interactor = GetUsersForItems(
        storage=storage,
        presenter=presenter
        )

    # act
    actual_response = interactor.get_users_for_items_interactor(
        item_id=item_id,
        offset=offset,
        limit=limit
        )

    # assert
    storage.get_users_for_items.assert_called_once_with(
        item_id=item_id,
        offset=offset,
        limit=limit
        )
    presenter.get_user_for_items_response.assert_called_once_with(
        get_item_users
        )
    storage.check_for_valid_input.assert_called_once_with([item_id,limit])
    assert expected_response[0]["person_name"] == actual_response[0]["person_name"]
    assert expected_response[0]["department"] == actual_response[0]["department"]
    assert expected_response[0]["job_role"] == actual_response[0]["job_role"]
    assert expected_response[0]["access_level"] == actual_response[0]["access_level"]

@pytest.mark.parametrize("item_id", [
    (1),(0)
])
def test_get_item_related_user_with_invalid_datad(
    get_item_users,
    get_item_users_response,
    item_id
    ):

    # arrange
    offset = 0
    limit = 1

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    storage.check_for_valid_input.return_value = False
    presenter.raise_invalid_id_exception.side_effect = NotFound
    storage.get_users_for_items.return_value = get_item_users
    presenter.get_user_for_items_response.return_value = \
                get_item_users_response

    interactor = GetUsersForItems(
        storage=storage,
        presenter=presenter
        )

    # act
    with pytest.raises(NotFound):
        interactor.get_users_for_items_interactor(
            item_id=item_id,
            offset=offset,
            limit=limit
            )

