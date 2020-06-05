# pylint: disable=wrong-import-position

APP_NAME = "resource_management"
OPERATION_NAME = "change_user_password"
REQUEST_METHOD = "post"
URL_SUFFIX = "change/user/password/"

from .test_case_01 import TestCase01ChangeUserPasswordAPITestCase

__all__ = [
    "TestCase01ChangeUserPasswordAPITestCase"
]
