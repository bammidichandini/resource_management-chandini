from abc import ABC
from typing import List
from abc import abstractmethod
from user_auth.dtos.dtos import userdto
from common.dtos import UserAuthTokensDTO


class StorageInterface(ABC):

    @abstractmethod
    def validate_username(self, username: str):
        pass

    @abstractmethod
    def validate_password(self,
                          username: str,
                          password: str
                          ):
        pass

    @abstractmethod
    def is_user_exists(self,username: str):
        pass

    @abstractmethod
    def create_a_new_user(self,
                          username: str,
                          password: str
                          ) -> int:
        pass

    @abstractmethod
    def is_admin(self, user_id: int) -> bool:
        pass

    # @abstractmethod
    # def check_for_valid_offset(self, offset):
    #   pass

    @abstractmethod
    def get_user_details_dtos(self, user_ids: List[int]) -> List[userdto]:
        pass

    @abstractmethod
    def get_user_ids(self) -> List[int]:
        pass

    @abstractmethod
    def get_all_user_details_to_admin(self) -> List[userdto]:
        pass
