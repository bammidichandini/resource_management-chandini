import datetime
import pytest
from common.dtos import (
    UserAuthTokensDTO,
    AccessTokenDTO,
    RefreshTokenDTO,
    Application
    )
from user_auth.dtos.dtos import(
    userdto,
    UpdateProfileDto,
    RegisterUserDto
    )
from user_auth.constants.enums import (
    Gender
    )
from user_auth.models import User
from django.contrib.auth.hashers import make_password



@pytest.fixture()
def access_dto():
    access_dto = AccessTokenDTO(
        access_token_id=1,
        token="12345",
        expires=datetime.datetime(2019, 4, 22, 0, 0)
        )
    return access_dto

@pytest.fixture()
def refresh_token_dto():
    refresh_dto = RefreshTokenDTO(
        token="12345",
        access_token="12345",
        user_id=1,
        revoked=datetime.datetime(2019, 4, 22, 0, 0)

        )
    return refresh_dto

@pytest.fixture()
def application_dto():
    applicationdto = Application(
        application_id=1
        )
    return applicationdto

@pytest.fixture()
def user_auth_tokens_dto():
    user_auth_tokens_dto = UserAuthTokensDTO(
        user_id=1,
        access_token="12345",
        refresh_token="12345",
        expires_in=datetime.datetime(2019, 4, 22, 0, 0)
    )

    return user_auth_tokens_dto

@pytest.fixture()
def login_response():
    response = {
        "role": True,
        "access_token": {
            "user_id": 1,
            "access_token": "12345",
            "refresh_token": "56789",
            "expires_in": datetime.datetime(2019, 4, 22, 0, 0)
        }
    }
    return response


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
            id=1,
            person_name="madhuri",
            job_role="backend_developer",
            department="engineer",
            profile_pic=""
            )
        ]
    return details


@pytest.fixture()
def user_response():
    get_response =[{
        "id": 1,
        "person_name": "madhuri",
        "department": "engineer",
        "job_role": "backend_developer",
        "profile_pic": ""
    },

    ]
    return get_response



@pytest.fixture()
def user_dtos():
    response = [
        userdto(
            id=1,
            person_name="chandini",
            department="department",
            profile_pic="chandini",
            job_role="job_role",
            is_admin=True
        )
    ]
    return response


@pytest.fixture()
def user_dtos1():
    response = [
        userdto(
            id=1,
            person_name="chandini",
            profile_pic="chandini",
            department="department",
            job_role="job_role",
            is_admin=False
        )
    ]
    return response
