# pylint: disable=wrong-import-position

APP_NAME = "resource_management"
OPERATION_NAME = "get_user_requests"
REQUEST_METHOD = "get"
URL_SUFFIX = "get/user/requests/"

from .test_case_01 import TestCase01GetUserRequestsAPITestCase

__all__ = [
    "TestCase01GetUserRequestsAPITestCase"
]
