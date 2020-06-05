# pylint: disable=wrong-import-position

APP_NAME = "resource_management"
OPERATION_NAME = "delete_resources"
REQUEST_METHOD = "post"
URL_SUFFIX = "delete/resources/"

from .test_case_01 import TestCase01DeleteResourcesAPITestCase

__all__ = [
    "TestCase01DeleteResourcesAPITestCase"
]
