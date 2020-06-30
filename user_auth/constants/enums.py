from ib_common.constants import BaseEnumClass
import enum



class Gender(BaseEnumClass, enum.Enum):
    Male = "MALE"
    Female = "FEMALE"


class TimeFormat(enum.Enum):
    FORMAT = '%Y-%m-%d %H:%M:%S.%f'
