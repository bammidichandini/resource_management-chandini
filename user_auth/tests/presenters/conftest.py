import datetime
import pytest
from common.dtos import (
    UserAuthTokensDTO,
    AccessTokenDTO,
    RefreshTokenDTO,
    Application
    )
from user_auth.dtos.dtos \
    import (
        userdto,
        RegisterUserDto
    )
from user_auth.constants.enums import TimeFormat

format = TimeFormat.FORMAT.value

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
        user_id="chandini",
        access_token="12345",
        refresh_token="56789",
        expires_in=datetime.datetime(2019, 4, 22, 0, 0)
    )

    return user_auth_tokens_dto

@pytest.fixture()
def resource_dto():
    resource_dtos = [ResourceDto(
    id=1,
    image_url="aws/cloud/aws.png",
    name= "aws",
    item_name= "cloud_services",
    link= "https://www.aws.com",
    description= "it provides cloud services"
    )]
    return resource_dtos

@pytest.fixture()
def item_dto():
    items_dto =[Itemdto(
        id=1,
        item_name="cloud",
        link="https://www.aws.in/cloud_services",
        resource_name="aws",
        access_level="Read"
        )]
    return items_dto


@pytest.fixture()
def get_resources_response():

    get_resources_response =[ {
        "id": 1,
        "image_url":"aws/cloud/aws.png",
        "name": "aws",
        "item_name": "cloud_services",
        "link": "https://www.aws.com",
        "description": "it provides cloud services"
    }]
    return get_resources_response


@pytest.fixture()
def get_resource_items_response():

    get_resource_items_response =[
        {
        "item_name": "cloud",
        "link": "https://www.aws.in/cloud_services",
        "resource_name": "aws",
        "description": "service provided by aws",
        "access_level": AccessLevel.Read.value
        }
        ]
    return get_resource_items_response

@pytest.fixture()
def get_login_response():

    get_login_response = {
        "user_id": "chandini",
        "access_token": "12345",
        "refresh_token": "56789",
        "expires_in": "2019-04-22 00:00:00.000000"
    }
    return get_login_response

@pytest.fixture()
def get_item_users_response():
    response =[ {
        "person_name": "chandini",
        "department": "engineer",
        "job_role": "backend_developer",
        "access_level": "Read"
    }]
    return response

@pytest.fixture()
def get_item_users():
    item_users = [UserDto(
            person_name="chandini",
            department="engineer",
            job_role="backend_developer",
            access_level="Read")
        ]
    return item_users

@pytest.fixture()
def requests():
    request = [{
        "name":"chandini",
        "access_level": "Read",
        "duedatetime":"2019-04-22 00:00:00.000000",
        "resource_name": "aws",
        "item_name": "cloud"
    }]
    return request

@pytest.fixture()
def get_requests():
    request_dto = [RequestsDto(
        access_level=AccessLevel.Read.value,
        duedatetime=datetime.datetime(2019, 4, 22, 0, 0),
        resource_name="aws",
        item_name="cloud",
        id=1,
        user_id=1
            )]
    return request_dto

@pytest.fixture()
def user_response():
    get_response =[
    {
            "person_name": "chandini",
            "department": "engineer",
            "job_role": "backend_developer",
            "profile_pic": ""
        }
    ]
    return get_response


@pytest.fixture()
def user_details():
    details = [
        RegisterUserDto(
            id=1,
            person_name="chandini",
            job_role="backend_developer",
            department="engineer",
            profile_pic=""
            )
        ]
    return details


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
            "department":"department",
            "job_role":"job_role",
            "profile_pic":"chandini",
            "resource_name":"aws",
            "item_name":"cloud",
            "access_level":"access_level",
            "description":"cloud services",
            "link":"https://www.aws.com"
    }]
    return response

@pytest.fixture
def get_request_response():
    return {
            "count": 3,
            "users": [{
                "id": 1,
                "person_name":"chandini",
                "department":"department",
                "job_role":"job_role",
                "access_level":"access_level"

            }]
        }


@pytest.fixture
def request_dto():
    response = [RequestDto(
        id=1,
        access_level="access_level"
        )]
    return response

@pytest.fixture()
def get_user_requests_dto():
    response =getuserrequestsdto(
    count=3,
    requests= [GetUserRequestsDto(
            id=1,
            resource_name="aws",
            item_name="service",
            access_level="Read",
            status="Pending"
        )])
    return response


@pytest.fixture()
def get_user_requests_dto_response():
    response = {
        "count": 3,
        "requests": [{
            "id":1,
            "resource_name":"aws",
            "item_name":"service",
            "access_level":"Read",
            "status":"Pending"
        }]
        }
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

