# pylint: disable=wrong-import-position

APP_NAME = "resource_management"
OPERATION_NAME = "status_accept"
REQUEST_METHOD = "post"
URL_SUFFIX = "request/status/"

from .test_case_01 import TestCase01StatusAcceptAPITestCase

__all__ = [
    "TestCase01StatusAcceptAPITestCase"
]
