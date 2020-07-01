import factory
from user_auth.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    name = factory.Sequence(lambda n: "name %03d" % n)
    profile_pic = factory.LazyAttribute(lambda obj: f"https://www.{obj.name}.png")
    email = factory.LazyAttribute(lambda obj: f"{obj.name}123@gmail.com")
    is_admin = factory.Iterator([True, False])
    gender = factory.Iterator(["MALE", "FEMALE"])
    job_role = factory.Iterator(["engineer", "police", "doctor"])
    department = factory.Iterator(["police", "doctor", "engineer"])
