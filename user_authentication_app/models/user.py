from django.contrib.auth.models import AbstractUser
from django.db import models
from user_authentication_app.constants.enum import Gender



class User(AbstractUser):
    name = models.CharField(max_length=50)
    profile_pic = models.URLField(max_length=200)
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


