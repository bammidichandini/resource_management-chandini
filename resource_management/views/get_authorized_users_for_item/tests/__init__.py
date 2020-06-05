# pylint: disable=wrong-import-position

APP_NAME = "resource_management"
OPERATION_NAME = "get_authorized_users_for_item"
REQUEST_METHOD = "get"
URL_SUFFIX = "get/item/users/"

from .test_case_01 import TestCase01GetAuthorizedUsersForItemAPITestCase

__all__ = [
    "TestCase01GetAuthorizedUsersForItemAPITestCase"
]
