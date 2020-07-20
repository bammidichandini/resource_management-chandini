import enum

from ib_common.constants import BaseEnumClass


class Boolean(enum.Enum):
    true = True
    false = False

class Gender(BaseEnumClass, enum.Enum):
    Male = "MALE"
    Female = "FEMALE"


class AccessLevel(enum.Enum):
    Read = "Read"
    Write = "Write"
    Read_and_Write = "Read_and_Write"

class RequestAccessLevel(enum.Enum):
   Product_Design = "Product_Design"
   Engineering = "Engineering"
   Marketing = "Marketing"

class TimeFormat(enum.Enum):
    FORMAT = '%Y-%m-%d %H:%M:%S.%f'

class RequestStatus(enum.Enum):
    Accepted = "Accepted"
    Rejected = "Rejected"
    Pending = "Pending"


class SortByEnums(enum.Enum):
    ASC = "ASCENDING"
    DESC = "DESCENDING"




