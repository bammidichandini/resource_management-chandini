from django.contrib.auth.models import AbstractUser
from django.db import models
from resource_management.constants.enums import Gender
from resource_management.models.resource \
    import Resource


class User(AbstractUser):
    name = models.CharField(max_length=50)
    profile_pic = models.CharField(max_length=50)
    email = models.EmailField(max_length=250, default=None, null=True)
    is_admin = models.BooleanField(default=False)

    Gender_Choice = (
        (Gender.Male.value, Gender.Male.value),
        (Gender.Female.value, Gender.Female.value)
        )

    gender = models.CharField(max_length=50, choices=Gender_Choice,
                                     default=None, null=True)

    job_role = models.CharField(max_length=50, default=None, null=True)

    department = models.CharField(max_length=50, default=None, null=True)
