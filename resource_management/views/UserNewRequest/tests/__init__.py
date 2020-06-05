# pylint: disable=wrong-import-position

APP_NAME = "resource_management"
OPERATION_NAME = "UserNewRequest"
REQUEST_METHOD = "post"
URL_SUFFIX = "v1/user/request/"

from .test_case_01 import TestCase01UserNewRequestAPITestCase

__all__ = [
    "TestCase01UserNewRequestAPITestCase"
]
