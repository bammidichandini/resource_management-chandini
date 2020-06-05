# pylint: disable=wrong-import-position

APP_NAME = "resource_management"
OPERATION_NAME = "UserUpdateRequest"
REQUEST_METHOD = "post"
URL_SUFFIX = "v2/user/{request_id}/request/"

from .test_case_01 import TestCase01UserUpdateRequestAPITestCase

__all__ = [
    "TestCase01UserUpdateRequestAPITestCase"
]
