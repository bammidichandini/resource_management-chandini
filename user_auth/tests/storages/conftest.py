import datetime
from user_auth.models import User
from django.contrib.auth.hashers import make_password
from user_auth.constants.enums import (
    Gender
    )
from user_auth.dtos.dtos import (
    userdto,
    UpdateProfileDto,
    RegisterUserDto,
    )
import pytest


@pytest.fixture()
def create_users1():
    users = [
        {
            "username": "madhuri",
            "name": "madhuri",
            "is_admin": "True",
            "password": "madhuri",
            "department": "engineer",
            "job_role": "backend_developer"
        },
        {
            "username": "chandini",
            "name": "chandini",
            "is_admin": "False",
            "password": "chandini",
            "department": "engineer",
            "job_role": "backend_developer"
        }
    ]

    for user in users:
        User.objects.create_user(
            username=user["username"],
            name=user["name"],
            is_admin=user["is_admin"],
            password=user["password"],
            department=user["department"],
            job_role=user["job_role"]
            ),


@pytest.fixture()
def update_user_profile():
    profile = UpdateProfileDto(
        id=1,
        name="Suman",
        email="suman@gmail.com",
        gender=Gender.Male.value,
        job_role="Full_stack developer",
        department="software"
    )
    return profile


@pytest.fixture()
def user_details():
    details = [
        RegisterUserDto(
            person_name="chandini",
            job_role="backend_developer",
            department="engineer",
            url=""
            )
        ]
    return details

