import pytest
from unittest.mock import create_autospec
from resource_management.exceptions.exceptions import (
    InvalidIdException,
    InvalidDetailsException
    )
from django_swagger_utils.drf_server.exceptions import NotFound
from resource_management.interactors.storages.requests_storage_interface \
    import StorageInterface
from resource_management.interactors.presenters.presenter_interface \
    import PresenterInterface
from resource_management.interactors.update_user_request_interactor \
    import UpdateUserRequestInteractor


@pytest.mark.parametrize("request_id", [
    (100),(30)])
@pytest.mark.django_db
def test_update_user_request_invalid_id(
    request_update_dto,
    request_id
):

    # arrange

    user_id = 1
    update_dto = request_update_dto

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    storage.get_request_ids.return_value = [1,2]
    presenter.raise_invalid_id_exception.side_effect = NotFound
    # storage.update_user_request.side_effect = NotFound
    interactor = UpdateUserRequestInteractor(
        storage=storage,
        presenter=presenter
        )

    # act
    with pytest.raises(NotFound):
        interactor.update_user_request_interactor(
            user_id=user_id,
            update_dto=update_dto,
            request_id=request_id
            )

    # assert
    storage.get_request_ids.assert_called_once()



@pytest.mark.django_db
def test_update_user_request(
    request_update_dto
):

    # arrange

    user_id = 1
    request_id = 1
    update_dto = request_update_dto

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    storage.get_request_ids.return_value = [1,2]
    storage.update_user_request.return_value = update_dto

    interactor = UpdateUserRequestInteractor(
        storage=storage,
        presenter=presenter
        )

    # act
    interactor.update_user_request_interactor(
        user_id=user_id,
        update_dto=update_dto,
        request_id=request_id
        )

    # assert
    storage.update_user_request.assert_called_once_with(
        user_id=user_id,
        request_id=request_id,
        update_dto=update_dto
    )
    storage.get_request_ids.assert_called_once()
