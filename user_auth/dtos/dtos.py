import datetime
from dataclasses import dataclass
from typing import Optional, List
# from user_auth.constants.enums import AccessLevel, RequestStatus



@dataclass
class userdto:
    id: Optional[int]
    person_name: str
    department: str
    job_role: str
    profile_pic: str
    is_admin: bool

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
    profile_pic: str
