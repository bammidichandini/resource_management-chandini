import datetime
from dataclasses import dataclass
from typing import Optional, List
from resource_management.constants.enums import AccessLevel, RequestStatus


@dataclass
class ResourceDto:
    id: Optional[int]
    image_url: str
    name: str
    item_name: str
    link: str
    description: str

@dataclass
class ItemDto:
    item_name: str
    link: str
    resource_name: str
    description: str

@dataclass
class userdto:
    id: Optional[int]
    person_name: str
    department: str
    job_role: str
    access_level: AccessLevel

@dataclass
class UserDto:
    count: int
    users: List[userdto]

@dataclass
class RequestsDto:
    id: Optional[int]
    name: str
    access_level: AccessLevel
    duedatetime: datetime.datetime
    resource_name: str
    item_name: str
    url: str
    id: int

@dataclass
class RequestsUpdateDto:
    id: Optional[int]
    access_level: AccessLevel
    duedatetime: datetime.datetime
    remarks: str
    resource_name: str
    item_name: str
    access_reason: str

@dataclass
class itemdto:
    item_id: Optional[int]
    item_name: str
    link: str
    description: str


@dataclass
class ResourceItemDto:
    id: int
    resource_name: str
    link: str
    description: str
    image_url: str
    item: List[itemdto]
    items_count: int



@dataclass
class ResourceItemParametersDto:
    resource_id: int
    offset: int
    limit: int

@dataclass
class UpdateProfileDto:
    id: Optional[int]
    name: str
    email: str
    gender: str
    job_role: str
    department: str


@dataclass
class RegisterUserDto:
    id: Optional[int]
    person_name: str
    department: str
    job_role: str
    url: str


@dataclass
class IndividualUserRequestsDto:
    id: Optional[int]
    person_name: str
    department: str
    job_role: str
    profile_pic: str
    resource_name: str
    item_name: str
    access_level: str
    description: str
    link: str


@dataclass
class CreateUserRequestsDto:
    access_level: AccessLevel
    duedatetime: datetime.datetime
    resource_name: str
    item_name: str
    access_reason: str


@dataclass
class GetUserRequestsDto:
    id: Optional[int]
    resource_name: str
    item_name: str
    access_level: AccessLevel
    status: RequestStatus

