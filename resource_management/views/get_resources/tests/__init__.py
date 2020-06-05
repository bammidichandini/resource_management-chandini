# pylint: disable=wrong-import-position

APP_NAME = "resource_management"
OPERATION_NAME = "get_resources"
REQUEST_METHOD = "get"
URL_SUFFIX = "get/resources/"

from .test_case_01 import TestCase01GetResourcesAPITestCase

__all__ = [
    "TestCase01GetResourcesAPITestCase"
]
