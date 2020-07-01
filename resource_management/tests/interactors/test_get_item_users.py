import pytest
from unittest.mock import create_autospec, patch
from resource_management.exceptions.exceptions import InvalidIdException
from django_swagger_utils.drf_server.exceptions import NotFound
from resource_management.interactors.get_item_accessible_user_interactor \
    import GetUsersForItems
from resource_management.interactors.storages.item_storages import StorageInterface
from resource_management.interactors.presenters.presenter_interface import PresenterInterface


@pytest.mark.django_db
@patch('resource_management.adapters.auth_service.AuthService.get_user_dtos')
def test_get_item_related_user(
    get_user_dtos,
    user_dtos,
    get_item_users,
    get_item_users_response
    ):

    # arrange

    item_id = 1
    offset = 0
    limit = 1
    expected_response = get_item_users_response

    get_user_dtos.return_value = user_dtos

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    storage.get_user_items_count.return_value = 3
    storage.get_item_ids.return_value = [1,2]
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
        request_dto=get_item_users,
        user_dtos=user_dtos,
        count=3
        )
    assert expected_response[0]["users"]["person_name"] == \
        actual_response[0]["users"]["person_name"]
    assert expected_response[0]["users"]["department"] == \
        actual_response[0]["users"]["department"]
    assert expected_response[0]["users"]["job_role"] == \
        actual_response[0]["users"]["job_role"]
    assert expected_response[0]["users"]["access_level"] == \
        actual_response[0]["users"]["access_level"]
    assert expected_response[0]["count"] == \
        actual_response[0]["count"]


@patch('resource_management.adapters.auth_service.AuthService.get_user_dtos')
@pytest.mark.django_db
@pytest.mark.parametrize("item_id", [
    (100),(20)
])
def test_get_item_related_user_with_invalid_datad(
    get_user_dtos,
    user_dtos,
    get_item_users,
    get_item_users_response,
    item_id
    ):

    # arrange

    offset = 0
    limit = 1

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    storage.get_user_items_count.return_value = 3
    storage.get_item_ids.return_value = [1,2]
    storage.get_users_for_items.return_value = get_item_users

    presenter.raise_invalid_id_exception.side_effect = NotFound
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
