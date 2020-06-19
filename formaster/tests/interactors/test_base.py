import pytest
from unittest.mock import create_autospec
from formaster.exceptions.exceptions import(
    FormExpired,
    FormDoesNotExist,
    InvalidQuestionId
)
from django_swagger_utils.drf_server.exceptions import NotFound
from formaster.interactors.storages.storage_interface import StorageInterface
from formaster.interactors.presenters.presenter_interface import PresenterInterface
from formaster.interactors.submit_form_response.base import SubmitFormResponseInteractor


def test_submit_form_raise_form_doesnot_exist_exception():

    # arrange
    form_id = 1
    user_id = 1
    question_id = 1

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    storage.is_form_live.return_value = True
    storage.check_for_form_id.side_effect = FormDoesNotExist
    presenter.raise_form_does_not_exist_exception.side_effect = NotFound

    wrapper = SubmitFormResponseInteractor(
        storage=storage,
        form_id=form_id,
        user_id=user_id,
        question_id=question_id
    )

    # act
    with pytest.raises(NotFound):
        wrapper.submit_form_response_wrapper(
            presenter=presenter
        )


    # assert
    storage.check_for_form_id.assert_called_once_with(form_id=form_id)
    storage.is_form_live.assert_called_once_with(form_id)
    presenter.raise_form_does_not_exist_exception.assert_called_once()


def test_submit_form_raise_form_closed_exception():

    # arrange
    form_id = 1
    user_id = 1
    question_id = 1

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    storage.is_form_live.side_effect = FormExpired
    presenter.raise_form_expired_exception.side_effect = NotFound

    wrapper = SubmitFormResponseInteractor(
        storage=storage,
        form_id=form_id,
        user_id=user_id,
        question_id=question_id
    )

    # act
    with pytest.raises(NotFound):
        wrapper.submit_form_response_wrapper(
            presenter=presenter
        )


    # assert
    storage.is_form_live.assert_called_once_with(form_id=form_id)
    presenter.raise_form_expired_exception.assert_called_once()


def test_submit_form_raise_invalid_question_id():

    # arrange
    form_id = 1
    user_id = 1
    question_id = 1

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    storage.validate_question_id_for_form_id.side_effect = InvalidQuestionId
    presenter.raise_invalid_question_id.side_effect = NotFound
    storage.is_form_live.return_value = True

    wrapper = SubmitFormResponseInteractor(
        storage=storage,
        form_id=form_id,
        user_id=user_id,
        question_id=question_id
    )

    # act
    with pytest.raises(NotFound):
        wrapper.submit_form_response_wrapper(
            presenter=presenter
        )


    # assert
    storage.validate_question_id_for_form_id.assert_called_once_with(
        form_id=form_id, question_id=question_id
    )
    storage.is_form_live.assert_called_once_with(form_id)
    presenter.raise_invalid_question_id.assert_called_once()
