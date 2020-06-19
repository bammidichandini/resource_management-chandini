from formaster.dtos.dtos import FormDto
from formaster.exceptions.exceptions import FormExpired


class ValidationMixin:

    def is_form_live(self, form_id: int):
        form_dto = self.storage.get_form_details(form_id=form_id)
        if not form_dto.is_live:
            raise FormExpired()
