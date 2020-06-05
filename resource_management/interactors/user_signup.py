from common.dtos import UserAuthTokensDTO
from common.oauth2_storage import OAuth2SQLStorage
from resource_management.interactors.storages.storage_interface \
    import StorageInterface
from resource_management.interactors.presenters.presenter_interface \
    import PresenterInterface
from common.oauth_user_auth_tokens_service import OAuthUserAuthTokensService


class UserSignUpInteractor:

    def __init__(self,
                 storage: StorageInterface,
                 oauth2_storage: OAuth2SQLStorage,
                 presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter
        self.oauth2_storage = oauth2_storage

    def user_signup_interactor(self,
                              username: str,
                              password: str
                              ):

        existed_user = self.storage.is_user_exists(
                username=username
                )

        if existed_user:
            self.presenter.raise_user_already_existed_exception()
            return

        else:
           user_id = self.storage.create_a_new_user(
                username=username,
                password=password
                )

        interactor = OAuthUserAuthTokensService(
            oauth2_storage=self.oauth2_storage
            )

        access_token_dto_obj = interactor.create_user_auth_tokens(
            user_id=user_id
            )

        response = self.presenter.get_signup_response(
            access_token_dto_obj=access_token_dto_obj
            )

        return response
