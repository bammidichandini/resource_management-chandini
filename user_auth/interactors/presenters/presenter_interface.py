from abc import ABC
from abc import abstractmethod
from typing import List
from common.dtos import UserAuthTokensDTO


class PresenterInterface(ABC):

    @abstractmethod
    def raise_invalid_password_exception(self):
        pass

    @abstractmethod
    def raise_invalid_username_exception(self):
        pass

    @abstractmethod
    def get_login_response(self,
                           access_token_dto_obj: UserAuthTokensDTO,
                           role: bool
                           ):
        pass

    @abstractmethod
    def raise_invalid_id_exception(self):
        pass

    # @abstractmethod
    # def get_signup_response(self,
    #                       access_token_dto_obj: UserAuthTokensDTO
    #                       ):
    #     pass

