# pylint: disable=wrong-import-position

APP_NAME = "resource_management"
OPERATION_NAME = "user_profile"
REQUEST_METHOD = "get"
URL_SUFFIX = "user/profile/"

from .test_case_01 import TestCase01UserProfileAPITestCase

__all__ = [
    "TestCase01UserProfileAPITestCase"
]
