# pylint: disable=wrong-import-position

APP_NAME = "resource_management"
OPERATION_NAME = "UserDeleteRequest"
REQUEST_METHOD = "delete"
URL_SUFFIX = "delete/user/{request_id}/request/"

from .test_case_01 import TestCase01UserDeleteRequestAPITestCase

__all__ = [
    "TestCase01UserDeleteRequestAPITestCase"
]
