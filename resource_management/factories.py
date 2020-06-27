import factory, factory.django, factory.fuzzy
from resource_management.models import (
    User,
    Resource,
    UserAccess,
    Request,
    Item
)
from resource_management.constants.enums import (
    Gender,
    Boolean,
    RequestAccessLevel
    )
import datetime


gender_choice = [Gender.Male.value, Gender.Female.value]

boolean_choice = [Boolean.true.value, Boolean.false.value]

job_role_choices = [RequestAccessLevel.Product_Design.value, RequestAccessLevel.Engineering.value, RequestAccessLevel.Marketing.value]

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: "chandini21%d" % n)
    name = factory.Sequence(lambda n: "name%d" % n)
    profile_pic = factory.LazyAttribute(lambda obj: f"https://www.{obj.username}.svg/")
    email = factory.LazyAttribute(lambda obj: f"{obj.username}.{obj.name}@gmail.com")
    is_admin = factory.Iterator(boolean_choice)
    gender = factory.Iterator(gender_choice)
    job_role = factory.Iterator(job_role_choices)
    department = factory.Iterator(job_role_choices)

class ResourceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Resource

    name = factory.Sequence(lambda n: "resource_name%d" % n)
    image_url = factory.LazyAttribute(lambda obj: f"https://www.{obj.name}.svg/")
    link = factory.LazyAttribute(lambda n: f"https://www.{n.name}.com/")
    item_name = factory.Sequence(lambda n: "item_name1%d" % n)
    description = factory.Sequence(lambda n: "description1%d" % n)

class ItemFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Item

    name = factory.Sequence(lambda n: "itemname1%d" % n)
    link = factory.LazyAttribute(lambda n: f"https://www.{n.name}.com/")
    description = factory.Sequence(lambda n: "description1%d" % n)
    resource = factory.Iterator(Resource.objects.all())

class RequestFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Request

    duration = factory.fuzzy.FuzzyNaiveDateTime(
        start_dt=datetime.datetime(2020, 1, 1),
        end_dt=datetime.datetime(2020, 2, 9)
    )

    reason = factory.Sequence(lambda n: "reason1%d" %n)
    user = factory.Iterator(User.objects.all())
    item = factory.Iterator(Item.objects.all())
    resource = factory.Iterator(Resource.objects.all())
    status = factory.Iterator(["Accepted", "Rejected", "Pending"])
    remarks = factory.Sequence(lambda n: "remarks1%d" % n)
    access_level = factory.Iterator(["Read", "Write", "Read_and_Write"])


class UserWithRequestFactory(UserFactory):

    user_request = factory.RelatedFactory(RequestFactory, 'user')

class UserWith2RequestsFactory(UserFactory):

    user_request1 = factory.RelatedFactory(RequestFactory, 'user')
    user_request2 = factory.RelatedFactory(RequestFactory, 'user')


class UserAccessFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = UserAccess

    item = factory.Iterator(Item.objects.all())
    user = factory.Iterator(User.objects.all())
    access_level = factory.Iterator(["Read", "Write", "Read_and_Write"])
