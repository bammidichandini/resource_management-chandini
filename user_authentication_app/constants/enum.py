import enum
from ib_common.constants import BaseEnumClass


class Gender(BaseEnumClass, enum.Enum):
    Male = "MALE"
    Female = "FEMALE"
