from unittest.mock import create_autospec
import pytest
from django_swagger_utils.drf_server.exceptions import NotFound
from resource_management.interactors.storages.requests_storage_interface import StorageInterface
from resource_management.interactors.presenters.presenter_interface import PresenterInterface
from resource_management.interactors.create_new_request_interactor import CreateNewRequestInteractor


@pytest.mark.django_db
def test_create_request(
    add_request_dto,
):

    # arrange

    user_id = 1
    add_request_dto = add_request_dto

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    interactor = CreateNewRequestInteractor(
        storage=storage,
        presenter=presenter
        )

    # act
    interactor.create_new_request_interactor(
        user_id=user_id,
        request_dto=add_request_dto
        )

    # assert
    storage.create_new_user_request.assert_called_once_with(
        user_id=user_id,
        request_dto=add_request_dto
        )

