from common.dtos import UserAuthTokensDTO
from common.oauth2_storage import OAuth2SQLStorage
from common.oauth_user_auth_tokens_service import OAuthUserAuthTokensService
from user_authentication_app.storages.authentication_storage \
    import StorageImplementation
from user_authentication_app.presenters.authentication_presenter \
    import PresenterImplementation
from user_authentication_app.exceptions.custom_exceptions \
    import InvalidUserException, InvalidPasswordException


class UserLoginInteractor:


    def __init__(
        self,
        storage: StorageImplementation,
        oauth2_storage: OAuth2SQLStorage
    ):

        self.storage = storage
        self.oauth2_storage = oauth2_storage

    def user_login_wrapper(
            self,
            username: str,
            password: str,
            presenter: PresenterImplementation
    ):
        try:
            access_token_dto_obj, is_admin = self.user_login_interactor(
                username=username,
                password=password
            )
            print("*"*100)
            print(access_token_dto_obj)
            print(is_admin)
            return presenter.get_login_response(
                access_token_obj=access_token_dto_obj,
                is_admin=is_admin
            )
        except InvalidUserException:
            return presenter.raise_invalid_user_exception()


        except InvalidPasswordException:
            return presenter.raise_invalid_password_exception()


    def user_login_interactor(
        self,
        username: str,
        password: str
    ):


        self.storage.validate_username(
            username=username
            )


        user_id = self.storage.validate_password(
            username=username,
            password=password
            )



        interactor = OAuthUserAuthTokensService(
        oauth2_storage=self.oauth2_storage
        )

        access_token_dto_obj = interactor.create_user_auth_tokens(
        user_id=user_id
        )



        is_admin = self.storage.is_admin(user_id)

        return access_token_dto_obj, is_admin
