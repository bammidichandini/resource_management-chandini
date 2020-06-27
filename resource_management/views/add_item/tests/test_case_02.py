"""
# TODO: Update test case description
"""

from resource_management.utils.custom_test_utils import CustomTestUtils
from django_swagger_utils.utils.test import CustomAPITestCase
from resource_management.models import Item, UserAccess, Resource
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX

REQUEST_BODY = """
{
    "item_name": "string",
    "link": "string",
    "resource_name": "string",
    "access_level": "Read",
    "item_description": "string"
}
"""

TEST_CASE = {
    "request": {
        "path_params": {},
        "query_params": {},
        "header_params": {},
        "securities": {"oauth": {"tokenUrl": "http://auth.ibtspl.com/oauth2/", "flow": "password", "scopes": ["write"], "type": "oauth2"}},
        "body": REQUEST_BODY,
    },
}


class TestCase02AddItemAPITestCase(CustomTestUtils):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE
    import json
    request_body = json.loads(REQUEST_BODY)
    resource_name = request_body["resource_name"]
    item_name = request_body["item_name"]
    link = request_body["link"]
    access_level = request_body["access_level"]
    item_description = request_body["item_description"]

    def setupUser(self, username, password):
        super(TestCase02AddItemAPITestCase, self).setupUser(
            username=username, password=password
        )

        self.create_resource(name=self.resource_name)

    def test_case(self):
        self.default_test_case()
        # Returns response object.
        # Which can be used for further response object checks.
        # Add database state checks here.
