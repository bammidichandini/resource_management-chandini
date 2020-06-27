# pylint: disable=wrong-import-position

APP_NAME = "resource_management"
OPERATION_NAME = "create_resource"
REQUEST_METHOD = "post"
URL_SUFFIX = "v1/resource/"

from .test_case_01 import TestCase01CreateResourceAPITestCase
from .test_case_02 import TestCase02CreateResourceAPITestCase

__all__ = [
    "TestCase01CreateResourceAPITestCase",
    "TestCase02CreateResourceAPITestCase"
]
