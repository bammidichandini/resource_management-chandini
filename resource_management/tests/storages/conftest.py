from resource_management.models \
    import User, Resource, Item
from resource_management.models.item import \
    UserAccess, Request
import datetime
from django.contrib.auth.hashers import make_password
from resource_management.constants.enums import (
    AccessLevel,
    RequestStatus,
    Gender
    )
from resource_management.dtos.dtos import (
    ResourceDto, ItemDto, RequestsDto,
    ResourceItemDto, UserDto,
    ResourceItemParametersDto,
    UpdateProfileDto,
    RegisterUserDto,
    userdto,
    getuserrequestsdto,
    RequestsUpdateDto,
    IndividualUserRequestsDto,
    CreateUserRequestsDto,
    GetUserRequestsDto
    )
import pytest


@pytest.fixture()
def create_users():
    users = [
        {
            "username": "madhuri",
            "name": "madhuri",
            "is_admin": "True",
            "password": "madhuri",
            "profile_pic": "profile_pic_url1",
            "department": "engineer",
            "job_role": "backend_developer"
        },
        {
            "username": "chandini",
            "name": "chandini",
            "is_admin": "False",
            "password": "chandini",
            "profile_pic": "profile_pic_url2",
            "department": "engineer",
            "job_role": "backend_developer"
        }
    ]

    User.objects.create_user(
        [
            User(username=user["username"],
            password=make_password(user["password"]),
            name=user["name"],
            profile_pic=user["profile_pic"],
            department=user["department"],
            job_role=user["job_role"]
            )
            for user in users
        ]
    )

@pytest.fixture()
def create_items(create_resources,
                 create_users1
                 ):
    items = [
        {
        "item_name": "cloud",
        "link": "https://www.aws.in/cloud_services",
        "resource_name": "aws",
        "description": "service provided by aws",

        }
        ]
    resource = Resource.objects.get(id=1)
    for item in items:
        Item.objects.create(
            name=item["item_name"],
            link=item["link"],
            resource=resource,
            description=item["description"],
            )



@pytest.fixture()
def create_useraccess(create_users1,create_items):

    user = User.objects.get(id=1)
    access = [
        {
            "user": user,
            "item_id": 1,
            "access_level": "Read",
        }
        ]
    for aces in access:
        UserAccess.objects.create(
            user=aces["user"],
            item_id=aces["item_id"],
            access_level=aces["access_level"]
            )

@pytest.fixture()
def create_requests(create_useraccess, create_resources, create_users1):
    requests = [
        {
            "item": 1,
            "duration": datetime.datetime(2019, 4, 22, 0, 0),
            "status": RequestStatus.Pending.value,
            "reason": "want to access",
            "access_level": "Read"
        }
        ]
    for request in requests:
        Request.objects.create(
                item_id=request["item"],
                duration=request["duration"],
                reason=request["reason"],
                status=request["status"],
                access_level=request["access_level"],
                resource_id=1,
                user_id=1
                )

@pytest.fixture()
def create_resources():
    resources = [
        {
            "image_url": "aws/cloud/aws.png",
            "name": "aws",
            "item_name": "cloud_services",
            "link": "https://www.aws.com",
            "description": "it provides cloud services"
        }
        ]

    for resource in resources:
        Resource.objects.create(
            image_url=resource["image_url"],
            name=resource["name"],
            item_name=resource["item_name"],
            link=resource["link"],
            description=resource["description"]
            )


@pytest.fixture()
def request_dto():
    request = [
        RequestsDto(
            duration=datetime.datetime(2019, 4, 22, 0, 0),
            item_name="cloud",
            resource="aws",
            access_level="Read",
            id=1,
            url="https//www.aws.com"
            )
        ]
    return request

@pytest.fixture()
def request_response():
    get = {
                "name": "cloud",
                "access_level":"Read",
                "duedatetime":datetime.datetime(2019, 4, 22, 0, 0),
                "resource":"aws"
            }
    return get


@pytest.fixture()
def resource_dto():
    resource_dtos = [ResourceDto(
    image_url="aws/cloud/aws.png",
    name= "aws",
    item_name= "cloud_services",
    link= "https://www.aws.com",
    description= "it provides cloud services"
    )]
    return resource_dtos

@pytest.fixture()
def resource_dtos():
    resource_dtos = ResourceDto(
    image_url="https://www.github.com",
    name= "amazon",
    item_name= "cloud_services",
    link= "https://www.aws.com",
    description= "cloud service"
    )
    return resource_dtos

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
        User.objects.create(
            username=user["username"],
            name=user["name"],
            is_admin=user["is_admin"],
            password=make_password(user["password"]),
            department=user["department"],
            job_role=user["job_role"]
            ),


@pytest.fixture()
def item_dto():
    items_dto = [ResourceItemDto(
        item_name="cloud",
        link="https://www.aws.in/cloud_services",
        description="service provided by aws"
        )]
    return items_dto

@pytest.fixture()
def item_dtos():
    items_dto = ResourceItemDto(
        item_name="cloud",
        link="https://www.aws.in/cloud_services",
        description="service provided by aws"
        )
    return items_dto

@pytest.fixture()
def reitem_dto():
    items_dto = [ItemDto(
        item_name="cloud",
        link="https://www.aws.in/cloud_services",
        description="service provided by aws",
        resource_name="aws"
        )]
    return items_dto

@pytest.fixture()
def reitems_dto():
    items_dto = ItemDto(
        item_name="cloud",
        link="https://www.aws.in/cloud_services",
        description="service provided by aws",
        resource_name="aws"
        )
    return items_dto


@pytest.fixture()
def get_item_users():
    item_users = userdto(
            id=1,
            person_name="madhuri",
            department="engineer",
            job_role="backend_developer",
            access_level="Read")

    return item_users

@pytest.fixture()
def get_requests():
    request_dto = [RequestsDto(
        name="madhuri",
        access_level=AccessLevel.Read.value,
        duedatetime=datetime.datetime(2019, 4, 22, 0, 0),
        resource_name="aws",
        item_name="cloud",
        url="image_url",
        id=1,
        )]
    return request_dto

@pytest.fixture()
def get_req_param():
    param_dto = ResourceItemParametersDto(
        resource_id=1,
        offset=0,
        limit=1
        )
    return param_dto


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
            person_name="chandini",
            job_role="backend_developer",
            department="engineer",
            url=""
            )
        ]
    return details


@pytest.fixture()
def user_requests_dto():
    response = [IndividualUserRequestsDto(
            id=1,
            person_name="madhuri",
            department="engineer",
            job_role="backend_developer",
            profile_pic="",
            resource_name="aws",
            item_name="cloud",
            access_level="Read",
            description="service provided by aws",
            link="https://www.aws.in/cloud_services"
            )]
    return response



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
def request_update_dto():
    response = RequestsUpdateDto(
        id=1,
        access_level="Write",
        duedatetime=datetime.datetime(2019, 3, 1, 0, 0),
        remarks="accept your access",
        resource_name="aws",
        item_name="cloud",
        access_reason="want"
        )
    return response


@pytest.fixture()
def add_request_dto():
    response = CreateUserRequestsDto(
            access_level="Read",
            duedatetime=datetime.datetime(2019, 3, 1, 0, 0),
            resource_name="aws",
            item_name="cloud",
            access_reason="want"
    )
    return response

@pytest.fixture()
def add_request_dto_invalid_access_level():
    response = CreateUserRequestsDto(
            access_level=1,
            duedatetime=datetime.datetime(2019, 3, 1, 0, 0),
            resource_name="aws",
            item_name="service",
            access_reason="want"
    )
    return response

@pytest.fixture()
def add_request_dto_invalid_resource():
    response = CreateUserRequestsDto(
            access_level="Read",
            duedatetime=datetime.datetime(2019, 3, 1, 0, 0),
            resource_name=1,
            item_name="service",
            access_reason="want"
    )
    return response

@pytest.fixture()
def add_request_dto_invalid_item():
    response = CreateUserRequestsDto(
            access_level="Read",
            duedatetime=datetime.datetime(2019, 3, 1, 0, 0),
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
    response = getuserrequestsdto(
    count=1,
    requests=[GetUserRequestsDto(
            id=1,
            resource_name="aws",
            item_name="cloud",
            access_level="Read",
            status="Pending"
        )])
    return response


@pytest.fixture()
def get_user_requests_dto_response():
    response = [
        {
            "resource_name":"aws",
            "item_name":"cloud",
            "access_level":"Read",
            "status":"Pending"
        }
        ]
    return response
