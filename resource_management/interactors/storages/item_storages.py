from abc import ABC
from abc import abstractmethod
from typing import List
from common.dtos import UserAuthTokensDTO
from resource_management.dtos.dtos import (
    ItemDto,
    UserDto,
    RequestsDto,
    ResourceItemParametersDto
    )


class StorageInterface(ABC):

    @abstractmethod
    def create_item(
        self,
        item_dto: ItemDto,
        user_id: int
        ):
            pass

    @abstractmethod
    def delete_items(
        self,
        item_ids_list: List[int],
        user_id: int
        ):
        pass

    @abstractmethod
    def update_item(
        self,
        item_id: int,
        item_dto: ItemDto,
        user_id: int
        ):
        pass

    @abstractmethod
    def is_admin(self, user_id: int) -> bool:
        pass

    @abstractmethod
    def get_resource_items(self,
                           req_param_dto: ResourceItemParametersDto
                           ) -> List[ItemDto]:
        pass

    @abstractmethod
    def get_users_for_items(self, item_id: int) -> UserDto:
        pass

    @abstractmethod
    def get_requests(self) -> List[RequestsDto]:
        pass

    @abstractmethod
    def check_for_valid_input(self, item_ids_list: List[int]):
        pass