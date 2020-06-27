from freezegun import freeze_time
from django_swagger_utils.utils.test import CustomAPITestCase
from resource_management.models import *
from resource_management.factories import *


class CustomTestUtils(CustomAPITestCase):

    def create_resource(
        self, name
    ):
        ResourceFactory(name=name)

    def create_admin(self, user):
        user.is_admin = True
        user.save()

    def create_items(self):
        ResourceFactory.create_batch(size=5)
        ItemFactory.create_batch(size=5)

    def create_resources(self):
        ResourceFactory.create_batch(size=5)
