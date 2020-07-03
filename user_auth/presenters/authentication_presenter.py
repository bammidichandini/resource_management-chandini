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
from django_swagger_utils.drf_server.exceptions import \
    NotFound, BadRequest, Forbidden
# from user_auth.exceptions.exceptions import UserCannotManipulateException
from user_auth.constants.exception_messages import (
    INVALID_USER,
    INVALID_PASSWORD,
    FORBIDDEN,
    EXISTED_USER,
    INVALID_ID
)

class PresenterImplementation(PresenterInterface):

    def raise_invalid_password_exception(self):
        raise BadRequest(*INVALID_PASSWORD)


    def raise_invalid_username_exception(self):
        raise BadRequest(*INVALID_USER)


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

    def raise_user_already_existed_exception(self):
        raise BadRequest(*EXISTED_USER)

    def raise_invalid_id_exception(self):
        raise NotFound(*INVALID_ID)

    def get_signup_response(self,
                          access_token_dto_obj: UserAuthTokensDTO
                          ):
        format = TimeFormat.FORMAT.value
        dict = {
            "user_id": access_token_dto_obj.user_id,
            "access_token": access_token_dto_obj.access_token,
            "refresh_token": access_token_dto_obj.refresh_token,
            "expires_in": (access_token_dto_obj.expires_in).strftime(format)
        }

        return dict

