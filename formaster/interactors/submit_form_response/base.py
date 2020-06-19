from abc import abstractmethod
from formaster.exceptions.exceptions import (
    FormExpired,
    FormDoesNotExist,
    InvalidQuestionId
)
from formaster.interactors.mixins.form_validation import ValidationMixin
from formaster.interactors.storages.storage_interface import StorageInterface
from formaster.interactors.presenters.presenter_interface import PresenterInterface


class SubmitFormResponseInteractor(ValidationMixin):

    def __init__(
        self, question_id: int, form_id: int,
        user_id: int, storage: StorageInterface
    ):
        self.storage = storage
        self.form_id = form_id
        self.question_id = question_id
        self.user_id = user_id


    def submit_form_response_wrapper(self, presenter: PresenterInterface):
        try:
            return self.get_submit_form_response()
        except FormExpired:
            presenter.raise_form_expired_exception()
        except FormDoesNotExist:
            presenter.raise_form_does_not_exist_exception()
        except InvalidQuestionId:
            presenter.raise_invalid_question_id()


    def get_submit_form_response(
        self
    ):
        print("self---", self)
        #TODO: validate form live
        self.is_form_live(form_id=self.form_id)

        #TODO: validate question_id
        self.validate_question_id(
            form_id=self.form_id, question_id=self.question_id
        )

        #TODO: validate form_id
        self.validate_form_id(form_id=self.form_id)

        #TODO: validate user_response
        self.validate_user_response()

        #TODO: create user response
        response = self.create_user_response()

        return response

    @abstractmethod
    def validate_user_response(self):
        pass

    @abstractmethod
    def create_user_response(self) -> int:
        pass
