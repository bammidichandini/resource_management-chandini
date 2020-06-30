from abc import ABC
from abc import abstractmethod
from common.dtos import UserAuthTokensDTO
from user_auth.interactors.presenters.presenter_interface \
    import PresenterInterface
from typing import List
from user_auth.constants.enums import TimeFormat
from user_auth.dtos.dtos import (
    userdto
    )
from django_swagger_utils.drf_server.exceptions import NotFound
from resource_management.exceptions.exceptions import UserCannotManipulateException
from resource_management.exceptions.exceptions import (
    InvalidUserException,
    InvalidPasswordException,
    UserAlreadyExistedException,
    InvalidIdException,
    InvalidDetailsException
    )

class PresenterImplementation(PresenterInterface):

    def raise_invalid_password_exception(self):
        raise InvalidPasswordException


    def raise_invalid_username_exception(self):
        raise InvalidUserException


    def get_login_response(self,
                           access_token_dto_obj: UserAuthTokensDTO,
                           role: bool
                           ):
        format = TimeFormat.FORMAT.value
        dict = {
            "user_id": access_token_dto_obj.user_id,
            "access_token": access_token_dto_obj.access_token,
            "refresh_token": access_token_dto_obj.refresh_token,
            "expires_in": (access_token_dto_obj.expires_in).strftime(format)
        }
        result = {
            "role": role,
            "access_token": dict
        }
        return result

    def raise_invalid_id_exception(self, error: InvalidIdException):
        raise NotFound

    # def get_signup_response(self,
    #                       access_token_dto_obj: UserAuthTokensDTO
    #                       ):
    #     format = TimeFormat.FORMAT.value
    #     dict = {
    #         "user_id": access_token_dto_obj.user_id,
    #         "access_token": access_token_dto_obj.access_token,
    #         "refresh_token": access_token_dto_obj.refresh_token,
    #         "expires_in": (access_token_dto_obj.expires_in).strftime(format)
    #     }

    #     return dict

