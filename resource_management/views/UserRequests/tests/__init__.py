# pylint: disable=wrong-import-position

APP_NAME = "resource_management"
OPERATION_NAME = "UserRequests"
REQUEST_METHOD = "get"
URL_SUFFIX = "admin/user/requests/"

from .test_case_01 import TestCase01UserRequestsAPITestCase

__all__ = [
    "TestCase01UserRequestsAPITestCase"
]
