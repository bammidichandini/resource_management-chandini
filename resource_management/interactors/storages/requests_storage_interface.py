from abc import ABC
from abc import abstractmethod
from typing import List
from common.dtos import UserAuthTokensDTO
from resource_management.dtos.dtos import (
    RequestsDto,
    IndividualUserRequestsDto,
    RequestsUpdateDto,
    GetUserRequestsDto,
    CreateUserRequestsDto,
    getuserrequestsdto
    )


class StorageInterface(ABC):

    @abstractmethod
    def get_requests(self) -> List[RequestsDto]:
        pass


    @abstractmethod
    def set_status(
        self, status: str,
        request_ids_list: List[int],
        reason: str
        ):
        pass

    @abstractmethod
    def get_individual_user_details_to_admin(self, user_id: int) \
            -> IndividualUserRequestsDto:
        pass

    @abstractmethod
    def update_user_request(
        self,
        user_id: int,
        request_id: int,
        update_dto: RequestsUpdateDto ):
        pass

    @abstractmethod
    def delete_user_request(self, user_id: int, request_id: int):
        pass


    @abstractmethod
    def create_new_user_request(
        self,
        request_dto: CreateUserRequestsDto,
        user_id: int
    ):
        pass

    @abstractmethod
    def get_user_requests(self, user_id: int, offset, limit) -> getuserrequestsdto:
        pass

    @abstractmethod
    def is_admin(self, user_id: int) -> bool:
        pass

    @abstractmethod
    def check_for_valid_input(self, item_ids_list: List[int]) -> bool:
        pass

    @abstractmethod
    def check_for_valid_offset(self, offset):
       pass
