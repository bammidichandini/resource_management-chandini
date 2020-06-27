from common.dtos import UserAuthTokensDTO
from common.oauth2_storage import OAuth2SQLStorage
from common.oauth_user_auth_tokens_service import OAuthUserAuthTokensService
from resource_management.storages.authentication_storage \
    import StorageImplementation
from resource_management.presenters.authentication_presenter \
    import PresenterImplementation
from resource_management.exceptions.exceptions \
    import InvalidUserException, InvalidPasswordException


class UserLoginInteractor:


    def __init__(
        self,
        storage: StorageImplementation,
        oauth2_storage: OAuth2SQLStorage,
        presenter: PresenterImplementation
    ):

        self.storage = storage
        self.presenter = presenter
        self.oauth2_storage = oauth2_storage


    def user_login_interactor(
        self,
        username: str,
        password: str
    ):

        try:
            self.storage.validate_username(
                username=username
                )

        except InvalidUserException:
            self.presenter.raise_invalid_username_exception()
            return

        try:
           user_id = self.storage.validate_password(
                username=username,
                password=password
                )

        except InvalidPasswordException:
            self.presenter.raise_invalid_password_exception()
            return

        except InvalidUserException:
            self.presenter.raise_invalid_username_exception()
            return

        interactor = OAuthUserAuthTokensService(
            oauth2_storage=self.oauth2_storage
            )

        access_token_dto_obj = interactor.create_user_auth_tokens(
            user_id=user_id
            )

        is_admin = self.storage.is_admin(user_id)

        response = self.presenter.get_login_response(
            access_token_dto_obj=access_token_dto_obj,
            role=is_admin
            )

        return response
