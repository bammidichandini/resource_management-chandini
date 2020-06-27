"""
# TODO: Update test case description
"""

from resource_management.models import Item
from resource_management.utils.custom_test_utils import CustomTestUtils
from django_swagger_utils.utils.test import CustomAPITestCase
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX

REQUEST_BODY = """
{
    "items_ids_list": [1,2]
}
"""

TEST_CASE = {
    "request": {
        "path_params": {},
        "query_params": {},
        "header_params": {},
        "securities": {"oauth": {"tokenUrl": "http://auth.ibtspl.com/oauth2/", "flow": "password", "scopes": ["write", "read"], "type": "oauth2"}},
        "body": REQUEST_BODY,
    },
}


class TestCase04DeleteItemAPITestCase(CustomTestUtils):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE
    import json
    request_body = json.loads(REQUEST_BODY)
    item_ids = request_body["items_ids_list"]
    item_id1 = item_ids[0]
    item_id2 = item_ids[1]


    def setupUser(self, username, password):
        super(TestCase04DeleteItemAPITestCase, self).setupUser(
            username=username, password=password
        )

        self.create_items()


    def test_case(self):
        self.default_test_case() # Returns response object.
        # Which can be used for further response object checks.
        # Add database state checks here.
