import pytest
import datetime
from unittest.mock import create_autospec, patch
from user_authentication_app.tests.common_features.user_mock import get_user_dtos_mock as user_dtos_mock
from user_authentication_app.interactors.user_login import UserLoginInteractor
from user_authentication_app.exceptions.custom_exceptions import (
    InvalidUserException,
    InvalidPasswordException
)
from common.dtos import (
    AccessTokenDTO,
    RefreshTokenDTO,
    Application,
    UserAuthTokensDTO

)
from user_authentication_app.tests.factories import UserModelFactory as UserFactory
from django_swagger_utils.drf_server.exceptions import NotFound



class TestUserLogin:

    import pytest

    @pytest.fixture
    def storage_mock(self):
        from user_authentication_app.storages.authentication_storage \
        import StorageImplementation
        storage = create_autospec(StorageImplementation)
        return storage

    @pytest.fixture
    def presenter_mock(self):
        from user_authentication_app.presenters.authentication_presenter \
        import PresenterImplementation
        presenter = create_autospec(PresenterImplementation)
        return presenter

    @pytest.fixture
    def oauth_mock(self):
        from common.oauth2_storage import OAuth2SQLStorage
        oauth_storage = create_autospec(OAuth2SQLStorage)
        return oauth_storage


    @patch('common.oauth_user_auth_tokens_service.OAuthUserAuthTokensService.create_user_auth_tokens')
    def test_user_login_with_username(
        self,
        create_user_auth_tokens,
        storage_mock,
        presenter_mock,
        oauth_mock,
        snapshot
    ):

        # arrange

        username = "chandini"
        password = "chandini"
        role = True
        user_id = 1

        storage = storage_mock
        presenter = presenter_mock
        oauth2_storage = oauth_mock


        interactor = UserLoginInteractor(
            storage=storage,
            oauth2_storage=oauth2_storage
        )

        @pytest.fixture
        def user_auth_tokens_dto():
            user_auth_tokens_dto = UserAuthTokensDTO(
                user_id=1,
                access_token="12345",
                refresh_token="12345",
                expires_in=datetime.datetime(2019, 4, 22, 0, 0)
            )

            return user_auth_tokens_dto

        @pytest.fixture
        def login_response():
            response = {
                "role": True,
                "access_token": {
                    "user_id": 1,
                    "access_token": "12345",
                    "refresh_token": "56789",
                    "expires_in": datetime.datetime(2019, 4, 22, 0, 0)
                }
            }
            return response

        presenter.get_login_response.return_value = login_response
        storage.is_admin.return_value = role
        storage.validate_password.return_value = user_id

        @pytest.fixture
        def application_dto():
            applicationdto = Application(
                application_id=1
            )
            return applicationdto

        oauth2_storage.get_or_create_default_application.return_value \
            = application_dto, True

        @pytest.fixture
        def access_dto():
            access_dto = AccessTokenDTO(
                access_token_id=1,
                token="12345",
                expires=datetime.datetime(2019, 4, 22, 0, 0)
            )
            return access_dto


        oauth2_storage.create_access_token.return_value = access_dto

        @pytest.fixture
        def refresh_token_dto():
            refresh_dto = RefreshTokenDTO(
                token="12345",
                access_token="12345",
                user_id=1,
                revoked=datetime.datetime(2019, 4, 22, 0, 0)

            )
            return refresh_dto

        oauth2_storage.create_refresh_token.return_value = refresh_token_dto

        create_user_auth_tokens.return_value = access_dto


        # act

        login_response = interactor.user_login_wrapper(
            username=username,
            password=password,
            presenter=presenter
        )

        # assert

        storage.validate_username.assert_called_once_with(username)
        storage.validate_password.assert_called_once_with(
            username=username,
            password=password
        )
        presenter.get_login_response.assert_called_once_with(
            access_token_obj=access_dto,
            is_admin=role
        )
        snapshot.assert_match(login_response, "response")