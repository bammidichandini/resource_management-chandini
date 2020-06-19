import re
from formaster.dtos.dtos import FibResponseDto
from formaster.exceptions.exceptions import InvalidUserResponse
from formaster.interactors.submit_form_response.base import \
    SubmitFormResponseInteractor
from formaster.interactors.storages.storage_interface import StorageInterface


class FillInTheBlanksInteractor(SubmitFormResponseInteractor):

    def __init__(
      self, form_id: int, question_id: int,
      user_id: int, storage: StorageInterface,
      user_option: str
    ):
        super().__init__(storage=storage, form_id=form_id, question_id=question_id, user_id=user_id)
        self.user_option = user_option

    def validate_user_response(self):
        answers = self.storage.get_answers_for_question(self.question_id)
        user_option = self.user_option.casefold()
        user_option = re.sub(" ","",user_option)
        if not user_option == answers:
            raise InvalidUserResponse

    def create_user_response(self) -> int:
        user_response_dto = FibResponseDto(
            user_id=self.user_id,
            question_id=self.question_id,
            user_option=self.user_option
        )

        response = self.storage.create_fib_question_response(user_response_dto)

        return response
