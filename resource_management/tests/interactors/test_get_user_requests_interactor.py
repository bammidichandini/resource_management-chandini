from unittest.mock import create_autospec
import pytest
from django_swagger_utils.drf_server.exceptions import NotFound
from resource_management.interactors.storages.requests_storage_interface import StorageInterface
from resource_management.interactors.presenters.presenter_interface import PresenterInterface
from resource_management.interactors.get_user_requests_interactor import GetUserRequestsInteractor


@pytest.mark.django_db
def test_get_user_requests(
    get_user_requests_dto,
    get_user_requests_dto_response
):

    # arrange
    user_id = 1
    offset = 0
    limit = 1

    expected = get_user_requests_dto_response

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    storage.check_for_valid_input.return_value = True
    storage.check_for_valid_offset.return_value = True
    storage.get_user_requests.return_value = get_user_requests_dto
    presenter.get_user_requests_response.return_value = get_user_requests_dto_response

    interactor = GetUserRequestsInteractor(
        storage=storage,
        presenter=presenter
        )

    # act
    response = interactor.get_user_requests_interactor(
        user_id=user_id,
        offset=offset,
        limit=limit
    )

    # assert
    storage.get_user_requests.assert_called_once_with(
        user_id=user_id,
        offset=offset,
        limit=limit
    )
    presenter.get_user_requests_response(get_user_requests_dto)
    assert expected[0]["resource_name"] == response[0]["resource_name"]
    assert expected[0]["item_name"] == response[0]["item_name"]
    assert expected[0]["access_level"] == response[0]["access_level"]
    assert expected[0]["status"] == response[0]["status"]



@pytest.mark.django_db
@pytest.mark.parametrize("offset, limit", [
    ([-1,1]),([1,0]),([1,-1])
])
def test_get_user_requests_with_invalid_offset(
    get_user_requests_dto,
    get_user_requests_dto_response,
    offset,
    limit
):

    # arrange
    user_id = 1

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    presenter.raise_invalid_id_exception.side_effect = NotFound

    interactor = GetUserRequestsInteractor(
        storage=storage,
        presenter=presenter
        )

    # act
    with pytest.raises(NotFound):
        interactor.get_user_requests_interactor(
        user_id=user_id,
        offset=offset,
        limit=limit
    )

    # assert
    storage.get_user_requests.assert_called_once_with(
        user_id=user_id,
        offset=offset,
        limit=limit
    )
    presenter.get_user_requests_response(get_user_requests_dto)
