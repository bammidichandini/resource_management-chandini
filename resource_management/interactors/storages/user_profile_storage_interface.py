from abc import ABC
from abc import abstractmethod
from resource_management.dtos.dtos import UpdateProfileDto


class StorageInterface(ABC):

    @abstractmethod
    def update_user_details(self,
                            user_id: int,
                            user_profile_dto: UpdateProfileDto
                            ):
        pass

    @abstractmethod
    def update_password(self, user_id: int, password: str):
        pass