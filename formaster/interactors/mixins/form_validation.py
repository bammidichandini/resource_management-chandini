from formaster.dtos.dtos import FormDto
from formaster.exceptions.exceptions import (
    FormExpired,
    FormDoesNotExist
)


class ValidationMixin:

    def is_form_live(self, form_id: int):
        is_live = self.storage.is_form_live(form_id=form_id)
        if not is_live:
            raise FormExpired


    def validate_form_id(self, form_id: int):
        self.storage.check_for_form_id(form_id=form_id)


    def validate_question_id(self, form_id:int, question_id: int):
        self.storage.validate_question_id_for_form_id(
            form_id=form_id,
            question_id=question_id
        )
