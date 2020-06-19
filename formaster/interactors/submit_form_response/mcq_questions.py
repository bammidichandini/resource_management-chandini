from formaster.dtos.dtos import UserResponseDto
from formaster.exceptions.exceptions import InvalidUserResponse
from formaster.interactors.submit_form_response.base import \
    SubmitFormResponseInteractor
from formaster.interactors.storages.storage_interface import StorageInterface


class McqQuestionsInteractor(SubmitFormResponseInteractor):

    def __init__(
      self, form_id: int, question_id: int,
      user_id: int, storage: StorageInterface,
      user_option: int
    ):
        super().__init__(storage=storage, form_id=form_id, question_id=question_id, user_id=user_id)
        self.user_option = user_option

    def validate_user_response(self):
        options = self.storage.get_options_for_question(self.question_id)
        if self.user_option not in options:
            raise InvalidUserResponse

    def create_user_response(self) -> int:
        user_response_dto = UserResponseDto(
            user_id=self.user_id,
            question_id=self.question_id,
            user_option=self.user_option
        )

        response = self.storage.create_mcq_question_response(user_response_dto)

        return response
