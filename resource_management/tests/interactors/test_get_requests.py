import pytest
from unittest.mock import create_autospec, patch
from resource_management.interactors.storages.item_storages \
    import StorageInterface
from resource_management.interactors.presenters.presenter_interface \
    import PresenterInterface
from resource_management.interactors.get_requests_interactor \
    import GetRequestsInteractor
from resource_management.dtos.dtos import RequestsDto


@pytest.mark.django_db
@patch('resource_management.adapters.auth_service.AuthService.get_user_dtos')
def test_get_requests(
    get_user_dtos,
    get_requests,
    user_dtos,
    requests
    ):

    # arrange

    user_id = 1
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    get_user_dtos.return_value = user_dtos
    storage.get_requests.return_value = get_requests
    presenter.get_requests_response.return_value = requests

    interactor = GetRequestsInteractor(
        storage=storage,
        presenter=presenter
        )


    # act
    actual = interactor.get_requests_interactor(user_id=user_id)

    # assert
    storage.get_requests.assert_called_once()
    presenter.get_requests_response.assert_called_once_with(
        user_dtos=user_dtos,
        request_dto=get_requests
        )
    assert actual[0] == requests[0]