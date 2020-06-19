import pytest
from unittest.mock import create_autospec
from formaster.exceptions.exceptions import InvalidUserResponse
from django_swagger_utils.drf_server.exceptions import NotFound
from formaster.interactors.storages.storage_interface import StorageInterface
from formaster.interactors.presenters.presenter_interface import PresenterInterface
from formaster.interactors.submit_form_response.mcq_questions import McqQuestionsInteractor


def test_mcq_questions_repsonse_with_invalid_response():

    # arrange
    form_id = 1
    user_id = 1
    question_id = 1
    user_option = 2

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    storage.is_form_live.return_value = True
    storage.get_options_for_question.return_value = [1]

    wrapper = McqQuestionsInteractor(
        storage=storage,
        form_id=form_id,
        user_id=user_id,
        question_id=question_id,
        user_option=user_option
    )

    # act
    with pytest.raises(InvalidUserResponse):
        wrapper.submit_form_response_wrapper(
            presenter=presenter
        )

    # assert
    storage.is_form_live.assert_called_once_with(form_id)
    storage.check_for_form_id


def test_mcq_questions_repsonse_create_user_response():

    # arrange
    form_id = 1
    user_id = 1
    question_id = 1
    user_option = 1

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    storage.is_form_live.return_value = True
    storage.get_options_for_question.return_value = [1]
    storage.create_mcq_question_response.return_value = 1

    wrapper = McqQuestionsInteractor(
        storage=storage,
        form_id=form_id,
        user_id=user_id,
        question_id=question_id,
        user_option=user_option
    )

    # act
    response = wrapper.submit_form_response_wrapper(
           presenter=presenter
        )

    # assert
    assert response == 1
