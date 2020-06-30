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
