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


class TestCase01AddItemAPITestCase(CustomTestUtils):
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
        super(TestCase01AddItemAPITestCase, self).setupUser(
            username=username, password=password
        )

        self.create_admin(self.foo_user)
        self.create_resource(name=self.resource_name)

    def test_case(self):
        self.default_test_case()
        # Returns response object.
        # Which can be used for further response object checks.
        # Add database state checks here.

        resource = Resource.objects.get(name=self.resource_name)

        item = Item.objects.get(
            resource=resource,
            name=self.item_name,
            link=self.link,
            description=self.item_description
        )

        self.assert_match_snapshot(
            name="item_id",
            value=item.id
        )

        self.assert_match_snapshot(
            name="item_name",
            value=item.name
        )

        self.assert_match_snapshot(
            name="resource_name",
            value=item.resource_id
        )

        self.assert_match_snapshot(
            name="link",
            value=item.link
        )

        self.assert_match_snapshot(
            name="description",
            value=item.description
        )
