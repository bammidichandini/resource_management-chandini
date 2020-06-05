# pylint: disable=wrong-import-position

APP_NAME = "resource_management"
OPERATION_NAME = "login"
REQUEST_METHOD = "post"
URL_SUFFIX = "login/"

from .test_case_01 import TestCase01LoginAPITestCase

__all__ = [
    "TestCase01LoginAPITestCase"
]
