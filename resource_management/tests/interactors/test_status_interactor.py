import pytest
from unittest.mock import create_autospec
from resource_management.interactors.storages.requests_storage_interface import StorageInterface
from resource_management.interactors.presenters.presenter_interface import PresenterInterface
from resource_management.interactors.status_interactor import StatusInteractor
from resource_management.exceptions.exceptions import InvalidIdException



def test_status():

    # arrange

    request_ids_list = [1]
    status = "Accepted"
    reason = "something"

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    interactor = StatusInteractor(
        storage=storage,
        presenter=presenter
        )

    # act

    interactor.status_interactor(
        request_ids_list=request_ids_list,
        status=status,
        reason=reason
        )

    # assert
    storage.set_status.assert_called_once_with(
        request_ids_list=request_ids_list,
        reason=reason,
        status=status
        )


def test_status_with_invalid_id_raises_exception():

    # arrange

    request_ids_list = [-1]
    status = "Accepted"
    reason = "something"

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    storage.check_for_valid_input.return_value = False
    presenter.raise_invalid_id_exception.side_effect = InvalidIdException

    interactor = StatusInteractor(
        storage=storage,
        presenter=presenter
        )

    # act
    with pytest.raises(InvalidIdException):
        interactor.status_interactor(
                request_ids_list=request_ids_list,
                reason=reason,
                status=status
                )




def test_status_with_invalid_id_zero_raises_exception():

    # arrange

    request_ids_list = [0]
    status = "Accepted"
    reason = "something"

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    storage.check_for_valid_input.return_value = False
    presenter.raise_invalid_id_exception.side_effect = InvalidIdException

    storage.set_status.side_effect = InvalidIdException
    interactor = StatusInteractor(
        storage=storage,
        presenter=presenter
        )

    # act
    with pytest.raises(InvalidIdException):
        interactor.status_interactor(
                request_ids_list=request_ids_list,
                reason=reason,
                status=status
                )

