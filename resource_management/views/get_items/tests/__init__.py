# pylint: disable=wrong-import-position

APP_NAME = "resource_management"
OPERATION_NAME = "get_items"
REQUEST_METHOD = "get"
URL_SUFFIX = "get/{resource_id}/items/"

from .test_case_01 import TestCase01GetItemsAPITestCase

__all__ = [
    "TestCase01GetItemsAPITestCase"
]
