import abc
from abc import abstractmethod


class StorageInterface(abc.ABC):

    @abstractmethod
    def validate_username(self, username: str):
        pass


    @abstractmethod
    def validate_password(selfself, password: str):
        pass

    @abstractmethod
    def is_admin(self, user_id: int) -> bool:
        pass
