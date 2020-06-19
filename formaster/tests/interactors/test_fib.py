import pytest
from unittest.mock import create_autospec
from formaster.exceptions.exceptions import InvalidUserResponse
from django_swagger_utils.drf_server.exceptions import NotFound
from formaster.dtos.dtos import FibResponseDto
from formaster.interactors.storages.storage_interface import StorageInterface
from formaster.interactors.presenters.presenter_interface import PresenterInterface
from formaster.interactors.submit_form_response.fil_in_the_blanks \
    import FillInTheBlanksInteractor


def test_mcq_questions_repsonse_create_user_response():

    # arrange
    form_id = 1
    user_id = 1
    question_id = 1
    user_option = "chandini"
    user_response_dto = FibResponseDto(
            user_id=user_id,
            question_id=question_id,
            user_option=user_option
        )

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    storage.is_form_live.return_value = True
    storage.create_fib_question_response.return_value = 1

    wrapper = FillInTheBlanksInteractor(
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
    storage.is_form_live.assert_called_once_with(form_id)
    storage.check_for_form_id.assert_called_once_with(form_id)
    storage.validate_question_id_for_form_id.assert_called_once_with(
        form_id=form_id,
        question_id=question_id
    )
    storage.create_fib_question_response.assert_called_once_with(user_response_dto)
