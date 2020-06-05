# pylint: disable=wrong-import-position

APP_NAME = "resource_management"
OPERATION_NAME = "create_resources"
REQUEST_METHOD = "post"
URL_SUFFIX = "response/v1/"

from .test_case_01 import TestCase01CreateResourcesAPITestCase

__all__ = [
    "TestCase01CreateResourcesAPITestCase"
]
