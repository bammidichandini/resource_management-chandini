"""
# TODO: Update test case description
"""

from resource_management.utils.custom_test_utils import CustomTestUtils
from django_swagger_utils.utils.test import CustomAPITestCase
from resource_management.models import Resource
from resource_management.factories import ResourceFactory
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX

REQUEST_BODY = """
{
    "image_url": "string",
    "resource_name": "string",
    "item_name": "string",
    "link": "string",
    "description": "string",
    "is_admin": "string"
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


class TestCase02CreateResourceAPITestCase(CustomTestUtils):
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
    image_url = request_body["image_url"]
    description = request_body["description"]

    def setupUser(self, username, password):
        super(TestCase02CreateResourceAPITestCase, self).setupUser(
            username=username, password=password
        )


    def test_case(self):
        self.default_test_case() # Returns response object.
        # Which can be used for further response object checks.
        # Add database state checks here.

