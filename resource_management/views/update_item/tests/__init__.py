# pylint: disable=wrong-import-position

APP_NAME = "resource_management"
OPERATION_NAME = "update_item"
REQUEST_METHOD = "put"
URL_SUFFIX = "v2/{item_id}/items/"

from .test_case_01 import TestCase01UpdateItemAPITestCase

__all__ = [
    "TestCase01UpdateItemAPITestCase"
]
