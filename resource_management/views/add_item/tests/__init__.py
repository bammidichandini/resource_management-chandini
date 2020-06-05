# pylint: disable=wrong-import-position

APP_NAME = "resource_management"
OPERATION_NAME = "add_item"
REQUEST_METHOD = "post"
URL_SUFFIX = "v1/item/"

from .test_case_01 import TestCase01AddItemAPITestCase

__all__ = [
    "TestCase01AddItemAPITestCase"
]
