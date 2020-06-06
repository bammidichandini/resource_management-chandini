from abc import ABC
from abc import abstractmethod
from typing import List
from common.dtos import UserAuthTokensDTO
from resource_management.dtos.dtos import (
    ResourceDto,
    ItemDto,
    Itemdto,
    CreateUserRequestsDto
    )


class StorageInterface(ABC):

    @abstractmethod
    def check_for_valid_offset(self, offset):
       pass

    @abstractmethod
    def create_resource(self,
                        resource_dto: ResourceDto,
                        user_id: int
                        ):
        pass

    @abstractmethod
    def get_resources(self) -> List[ResourceDto]:
        pass

    @abstractmethod
    def update_resource(self, resource_id: int,
                        resource_dto: ResourceDto,
                        user_id: int
                        ):
        pass

    @abstractmethod
    def delete_resources(self,
                         user_id: int,
                         resource_ids_list: List[int]):
        pass

    @abstractmethod
    def get_user_resources(
        self,
        user_id: int
        ) -> List[Itemdto]:
        pass

    @abstractmethod
    def is_admin(self, user_id: int) -> bool:
        pass

    @abstractmethod
    def check_for_valid_input(self, item_ids_list: List[int]):
        pass