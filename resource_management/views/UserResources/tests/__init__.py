# pylint: disable=wrong-import-position

APP_NAME = "resource_management"
OPERATION_NAME = "UserResources"
REQUEST_METHOD = "get"
URL_SUFFIX = "user/resources/"

from .test_case_01 import TestCase01UserResourcesAPITestCase

__all__ = [
    "TestCase01UserResourcesAPITestCase"
]
