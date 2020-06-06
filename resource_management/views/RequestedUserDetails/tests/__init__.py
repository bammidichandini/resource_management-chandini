# pylint: disable=wrong-import-position

APP_NAME = "resource_management"
OPERATION_NAME = "RequestedUserDetails"
REQUEST_METHOD = "get"
URL_SUFFIX = "users/myrequests/"

from .test_case_01 import TestCase01RequestedUserDetailsAPITestCase

__all__ = [
    "TestCase01RequestedUserDetailsAPITestCase"
]
