from abc import ABC
from typing import List
from abc import abstractmethod
from formaster.dtos.dtos import UserResponseDto, FibResponseDto


class StorageInterface(ABC):

    @abstractmethod
    def is_form_live(self, form_id: int) -> bool:
        pass

    @abstractmethod
    def check_for_form_id(self, form_id: int):
        pass

    @abstractmethod
    def validate_question_id_for_form_id(
        self,
        form_id: int,
        question_id: int
    ):
        pass

    @abstractmethod
    def get_options_for_question(self, question_id: int) -> List[int]:
        pass

    @abstractmethod
    def create_mcq_question_response(
        self, user_response_dto: UserResponseDto
    ) -> int:
        pass

    @abstractmethod
    def create_fib_question_response(
        self, user_response_dto: FibResponseDto
    ) -> int:
        pass

    @abstractmethod
    def get_answers_for_question(self, answers: int) -> str:
        pass
