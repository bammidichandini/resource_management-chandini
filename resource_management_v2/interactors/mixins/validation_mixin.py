from resource_management_v2.exceptions.exceptions import InvalidOffsetOrLimit


class ValidationMixin:

    def validate_offset_and_limit(self, offset: int, limit: int):
        invalid_values = not offset < 0 or limit <= 0
        if invalid_values:
            raise InvalidOffsetOrLimit
