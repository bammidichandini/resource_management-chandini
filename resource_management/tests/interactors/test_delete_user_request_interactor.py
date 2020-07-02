import pytest
from unittest.mock import create_autospec
from django_swagger_utils.drf_server.exceptions import NotFound
from resource_management.interactors.storages.requests_storage_interface \
    import StorageInterface
from resource_management.interactors.presenters.presenter_interface \
    import PresenterInterface
from resource_management.interactors.delete_user_request \
    import DeleteUserRequestInteractor

@pytest.mark.parametrize("request_id", [
    (10),(20)])
@pytest.mark.django_db
def test_delete_user_request_invalid_id(
    request_id
):

    # arrange

    user_id = 1

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    storage.get_request_ids.return_value = [1,2]
    presenter.raise_invalid_id_exception.side_effect = NotFound

    interactor = DeleteUserRequestInteractor(
        storage=storage,
        presenter=presenter
        )

    # act
    with pytest.raises(NotFound):
        interactor.delete_user_request_interactor(
            user_id=user_id,
            request_id=request_id
            )


@pytest.mark.django_db
def test_update_user_request(
    request_update_dto
):

    # arrange

    user_id = 1
    request_id = 1

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    storage.get_request_ids.return_value = [1,2]

    interactor = DeleteUserRequestInteractor(
        storage=storage,
        presenter=presenter
        )

    # act
    interactor.delete_user_request_interactor(
        user_id=user_id,
        request_id=request_id
        )

    # assert
    storage.delete_user_request.assert_called_once_with(
        user_id=user_id,
        request_id=request_id
    )


