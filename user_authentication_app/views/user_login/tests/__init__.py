# pylint: disable=wrong-import-position

APP_NAME = "user_authentication_app"
OPERATION_NAME = "user_login"
REQUEST_METHOD = "post"
URL_SUFFIX = "login/v1/"

from .test_case_01 import TestCase01UserLoginAPITestCase

__all__ = [
    "TestCase01UserLoginAPITestCase"
]
