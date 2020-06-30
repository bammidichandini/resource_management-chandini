from abc import ABC
from abc import abstractmethod
from typing import List
from common.dtos import UserAuthTokensDTO
from resource_management.dtos.dtos import (
    ResourceDto,
    UserDto,
    RequestDto,
    RequestsDto,
    ResourceItemDto,
    userdto,
    RegisterUserDto,
    Itemdto,
    IndividualUserRequestsDto,
    getuserrequestsdto,
    ItemDto,
    GetUserRequestsDto
    )
from resource_management.exceptions.exceptions \
    import InvalidIdException


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
    def get_signup_response(self,
                           access_token_dto_obj: UserAuthTokensDTO
                           ):
        pass

    @abstractmethod
    def get_resources_response(
        self,
        resources_dto_list: List[ResourceDto]
        ):
        pass

    @abstractmethod
    def raise_user_cannot_manipulate_exception(self):
        pass

    @abstractmethod
    def get_resource_items_response(
        self,
        items_dto : ResourceItemDto
        ):
            pass


    @abstractmethod
    def get_user_for_items_response(
            self,
            request_dto: RequestDto,
            user_dtos: userdto,
            count: int
    ):
        pass

    @abstractmethod
    def get_requests_response(
        self,
        request_dto: List[RequestsDto],

        ):
        pass

    @abstractmethod
    def raise_user_already_existed_exception(self):
        pass


    @abstractmethod
    def raise_invalid_id_exception(self):
        pass

    @abstractmethod
    def raise_invalid_details_exception(self):
        pass

    @abstractmethod
    def get_user_details_to_admin_response(
        self,
        user_dto: List[RegisterUserDto]):
        pass

    @abstractmethod
    def get_individual_user_details_to_admin_response(self,
    user_requests_dto: List[IndividualUserRequestsDto],
    user_dto: userdto
    ):
        pass

    @abstractmethod
    def get_user_resources_response(self, items_dto: List[Itemdto]):
        pass

    @abstractmethod
    def get_user_requests_response(self, user_dto: getuserrequestsdto):
        pass
