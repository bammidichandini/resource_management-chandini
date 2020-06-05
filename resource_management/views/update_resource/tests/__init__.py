# pylint: disable=wrong-import-position

APP_NAME = "resource_management"
OPERATION_NAME = "update_resource"
REQUEST_METHOD = "put"
URL_SUFFIX = "v2/resource/{resource_id}/"

from .test_case_01 import TestCase01UpdateResourceAPITestCase

__all__ = [
    "TestCase01UpdateResourceAPITestCase"
]
