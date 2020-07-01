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
    def get_resource_items(self,
                           req_param_dto: ResourceItemParametersDto
                           ) -> List[ItemDto]:
        pass

    @abstractmethod
    def get_users_for_items(
        self,
        item_id: int,
        offset: int,
        limit: int
    ) -> UserDto:
        pass

    @abstractmethod
    def get_requests(self) -> List[RequestsDto]:
        pass


    @abstractmethod
    def get_item_ids(self):
        pass

    @abstractmethod
    def get_user_ids(
        self,
        item_id: int,
        offset: int,
        limit: int
    ) -> List[int]:
        pass

    @abstractmethod
    def get_user_items_count(
        self,
        item_id: int,
        offset: int,
        limit: int) -> int:
        pass
