# pylint: disable=wrong-import-position

APP_NAME = "resource_management"
OPERATION_NAME = "Userrelateditems"
REQUEST_METHOD = "get"
URL_SUFFIX = "individual/user/items/"

from .test_case_01 import TestCase01UserrelateditemsAPITestCase

__all__ = [
    "TestCase01UserrelateditemsAPITestCase"
]
