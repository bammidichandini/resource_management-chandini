"""
Created on 16/06/20

@author: revanth
"""


class FormValidationMixin:

    def validate_for_live_form(self, form_id: int):
        form_dto = self.storage.get_form(form_id)
        if not form_dto.is_live:
            raise FormClosed()
