import abc
from abc import abstractmethod
from user_authentication_app.interactors.presenter_interfaces.dtos import AccessTokenDTO


class PresenterInterface(abc.ABC):

    @abstractmethod
    def raise_invalid_user_exception(self):
        pass


    @abstractmethod
    def raise_invalid_password_exception(self):
        pass


    @abstractmethod
    def get_login_response(self, access_token_obj: AccessTokenDTO, is_admin: bool):
        pass
