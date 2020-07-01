import datetime
import pytest
from common.dtos import (
    UserAuthTokensDTO,
    AccessTokenDTO,
    RefreshTokenDTO,
    Application
    )
from resource_management.dtos.dtos import(
    ResourceDto,
    RequestDto,
    ItemDto,
    RequestsDto,
    userdto,
    UserDto,
    ResourceItemParametersDto,
    UpdateProfileDto,
    RegisterUserDto,
    IndividualUserRequestsDto,
    RequestsUpdateDto,
    CreateUserRequestsDto,
    GetUserRequestsDto
    )
from resource_management.constants.enums import (
    AccessLevel,
    Gender
    )
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
        refresh_token="56789",
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
def resource_dto():
    resource_dtos = [ResourceDto(
    id=1,
    image_url="aws/cloud/aws.png",
    name= "aws",
    item_name= "cloud_services",
    link= "https://www.aws.com",
    description= "cloud service"
    )]
    return resource_dtos


@pytest.fixture()
def resource_dtos():
    resource_dtos = ResourceDto(
        id=1,
        image_url="aws/cloud/aws.png",
        name= "aws",
        item_name= "cloud_services",
        link= "https://www.aws.com",
        description= "cloud service"
        )
    return resource_dtos

@pytest.fixture()
def item_dto():
    items_dto = ItemDto(
        item_name="cloud",
        link="https://www.aws.in/cloud_services",
        resource_name="aws",
        description="service provided by aws"
        )
    return items_dto


@pytest.fixture()
def items_dto():
    items_dto = [ItemDto(
        item_name="cloud",
        link="https://www.aws.in/cloud_services",
        resource_name="aws",
        description="service provided by aws"
        )]
    return items_dto


@pytest.fixture()
def get_resource():
    resource_dict = [{
        "id": 1,
        "image_url":"aws/cloud/aws.png",
        "name": "aws",
        "item_name": "cloud_services",
        "link": "https://www.aws.com",
        "description": "cloud service"
    }]
    return resource_dict

@pytest.fixture()
def get_item():
    item_dict =[
        {
        "item_name": "cloud",
        "link": "https://www.aws.in/cloud_services",
        "resource_name": "aws",
        "description": "service provided by aws",
        "access_level": AccessLevel.Read.value
        }
        ]
    return item_dict

@pytest.fixture()
def get_requests():
    request_dto = [RequestsDto(
        name="chandini",
        access_level=AccessLevel.Read.value,
        duedatetime=datetime.datetime(2019, 4, 22, 0, 0),
        resource_name="aws",
        item_name="cloud",
        id=1,
        url="https//www.aws.com"
            )]
    return request_dto

@pytest.fixture()
def requests():
    request = [{
        "name":"chandini",
        "access_level": "Read",
        "duedatetime":datetime.datetime(2019, 4, 22, 0, 0),
        "resource_name": "aws",
        "item_name": "cloud"
    }]
    return request


@pytest.fixture()
def get_item_users():
    item_users = [RequestDto(
            id=1,
            access_level="Read")
        ]
    return item_users

@pytest.fixture()
def get_item_users_response():
    response =[
        {
        "count": 3,
        "users": {
        "person_name": "chandini",
        "department": "engineer",
        "job_role": "backend_developer",
        "access_level": "Read",
        "id": 1
        }
    }]
    return response

@pytest.fixture()
def get_req_param():
    param_dto = ResourceItemParametersDto(
        resource_id=1,
        offset=1,
        limit=3
        )
    return param_dto


# @pytest.fixture()
# def create_users1():
#     users = [
#         {
#             "username": "madhuri",
#             "name": "madhuri",
#             "is_admin": "True",
#             "password": "madhuri",
#             "department": "engineer",
#             "job_role": "backend_developer"
#         },
#         {
#             "username": "chandini",
#             "name": "chandini",
#             "is_admin": "False",
#             "password": "chandini",
#             "department": "engineer",
#             "job_role": "backend_developer"
#         }
#     ]

#     for user in users:
#         User.objects.create(
#             username=user["username"],
#             name=user["name"],
#             is_admin=user["is_admin"],
#             password=make_password(user["password"]),
#             department=user["department"],
#             job_role=user["job_role"]
#             ),


@pytest.fixture()
def update_user_profile():
    profile = UpdateProfileDto(
        name="Suman",
        email="suman@gmail.com",
        gender=Gender.Male.value,
        job_role="Full_stack developer",
        department="software"
    )
    return profile

@pytest.fixture()
def update_profile_with_invalid_name():
    profile = UpdateProfileDto(
        name=1,
        email="suman@gmail.com",
        gender=Gender.Male.value,
        job_role="Full_stack developer",
        department="software"
    )
    return profile

@pytest.fixture()
def update_profile_with_invalid_email():
    profile = UpdateProfileDto(
        name="chandini",
        email=1,
        gender=Gender.Male.value,
        job_role="Full_stack developer",
        department="software"
    )
    return profile

@pytest.fixture()
def update_profile_with_invalid_gender():
    profile = UpdateProfileDto(
        name="Suman",
        email="suman@gmail.com",
        gender=1,
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
def user_requests_dto():
    response = [
        IndividualUserRequestsDto(
            id=1,
            resource_name="aws",
            item_name="cloud",
            access_level="access_level",
            description="cloud services",
            link="https://www.aws.com"
            )
        ]
    return response


@pytest.fixture()
def get_user_requests_response():
    response =  [{
            "person_name":"chandini",
            "department":"engineer",
            "job_role":"backend_developer",
            "profile_pic":"",
            "resource_name":"aws",
            "item_name":"cloud",
            "access_level":"access_level",
            "description":"cloud services",
            "link":"https://www.aws.com"
    }]
    return response


@pytest.fixture()
def request_update_dto():
    response = RequestsUpdateDto(
        id=1,
        access_level="Write",
        duedatetime=datetime.datetime(2019, 4, 22, 0, 0),
        remarks="accept your access",
        resource_name="amazon",
        item_name="cloud services",
        access_reason="want"
        )
    return response


@pytest.fixture()
def request_update_dto_invalid_access_level():
    response = RequestsUpdateDto(
        id=1,
        access_level=1,
        duedatetime=datetime.datetime(2019, 4, 22, 0, 0),
        remarks="accept your access",
        resource_name="amazon",
        item_name="cloud services",
        access_reason="want"
        )
    return response


@pytest.fixture()
def add_request_dto():
    response = CreateUserRequestsDto(
            access_level="Read",
            duedatetime=datetime.datetime(2019, 4, 22, 0, 0),
            resource_name="aws",
            item_name="service",
            access_reason="want"
    )
    return response

@pytest.fixture()
def add_request_dto_invalid_access_level():
    response = CreateUserRequestsDto(
            access_level=1,
            duedatetime=datetime.datetime(2019, 4, 22, 0, 0),
            resource_name="aws",
            item_name="service",
            access_reason="want"
    )
    return response

@pytest.fixture()
def add_request_dto_invalid_resource():
    response = CreateUserRequestsDto(
            access_level="Read",
            duedatetime=datetime.datetime(2019, 4, 22, 0, 0),
            resource_name=1,
            item_name="service",
            access_reason="want"
    )
    return response

@pytest.fixture()
def add_request_dto_invalid_item():
    response = CreateUserRequestsDto(
            access_level="Read",
            duedatetime=datetime.datetime(2019, 4, 22, 0, 0),
            resource_name="aws",
            item_name=1,
            access_reason="want"
    )
    return response

@pytest.fixture()
def add_request_dto_invalid_reason():
    response = CreateUserRequestsDto(
            access_level="Read",
            duedatetime=datetime.datetime(2019, 4, 22, 0, 0),
            resource_name="aws",
            item_name="service",
            access_reason=1
    )
    return response

@pytest.fixture()
def get_user_requests_dto():
    response = [GetUserRequestsDto(
            id=1,
            resource_name="aws",
            item_name="service",
            access_level="Read",
            status="Pending"
        )]
    return response


@pytest.fixture()
def get_user_requests_dto_response():
    response = [
        {
            "resource_name":"aws",
            "item_name":"service",
            "access_level":"Read",
            "status":"Pending"
        }
        ]
    return response

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
