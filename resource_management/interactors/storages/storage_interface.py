from abc import ABC
from abc import abstractmethod
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
