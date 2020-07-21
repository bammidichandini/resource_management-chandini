from common.dtos import UserAuthTokensDTO
from dataclasses import dataclass


@dataclass()
class AccessTokenDTO(UserAuthTokensDTO):
    access_token: UserAuthTokensDTO
    is_admin: bool
