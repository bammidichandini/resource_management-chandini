from unittest.mock import create_autospec
from resource_management.interactors.storages.storage_interface import StorageInterface
from resource_management.interactors.presenters.presenter_interface import PresenterInterface
from resource_management.interactors.user_login_interactor import UserLoginInteractor
from resource_management.storages.authentication_storage import StorageImplementation
from resource_management.presenters.authentication_presenter import PresenterImplementation
from common.oauth2_storage import OAuth2SQLStorage
from common.oauth_user_auth_tokens_service import OAuthUserAuthTokensService
from resource_management.interactors.user_login_interactor import UserLoginInteractor
from common.oauth2_storage import OAuth2SQLStorage
from common.oauth_user_auth_tokens_service import OAuthUserAuthTokensService
from django_swagger_utils.drf_server.exceptions import NotFound
import pytest


def test_login(user_auth_tokens_dto,
               access_dto,
               refresh_token_dto,
               application_dto
               ):

    #arrange
    username = "chandini"
    password = "chandini"
    user_id = 1

    storage = create_autospec(StorageImplementation)
    presenter = create_autospec(PresenterImplementation)
    oauth2_storage = create_autospec(OAuth2SQLStorage)

    interactor = UserLoginInteractor(
        storage=storage,
        oauth2_storage=oauth2_storage,
        presenter=presenter
        )
    presenter.get_login_response.return_value = user_auth_tokens_dto

    storage.validate_password.return_value = user_id
    oauth2_storage.get_or_create_default_application.return_value \
       = application_dto,True
    oauth2_storage.create_access_token.return_value = access_dto
    oauth2_storage.create_refresh_token.return_value = refresh_token_dto

    #act
    access_token_obj = interactor.user_login_interactor(
        username=username,
        password=password
        )

    #assert
    assert access_token_obj.user_id == user_auth_tokens_dto.user_id
    assert access_token_obj.access_token == user_auth_tokens_dto.access_token
    assert access_token_obj.refresh_token == user_auth_tokens_dto.refresh_token
    assert access_token_obj.expires_in == user_auth_tokens_dto.expires_in
    storage.validate_username.assert_called_once_with(username=username)
    storage.validate_password.assert_called_once_with(
        username=username,
        password=password
        )

def test_login_with_invalid_username(user_auth_tokens_dto,
                                     access_dto,
                                     refresh_token_dto,
                                     application_dto
                                     ):

    #arrange
    username = "ashwini"
    password = "chandini"

    storage = create_autospec(StorageImplementation)
    presenter = create_autospec(PresenterImplementation)
    oauth2_storage = create_autospec(OAuth2SQLStorage)

    interactor = UserLoginInteractor(
        storage=storage,
        oauth2_storage=oauth2_storage,
        presenter=presenter
        )
    presenter.get_login_response.return_value = user_auth_tokens_dto

    storage.validate_username.side_effect = NotFound
    #act
    with pytest.raises(NotFound):
        interactor.user_login_interactor(
            username=username,
            password=password
            )

    #assert
    storage.validate_username.assert_called_once_with(username=username)


def test_login_with_invalid_password(user_auth_tokens_dto,
                                     access_dto,
                                     refresh_token_dto,
                                     application_dto
                                     ):

    #arrange
    username = "admin"
    password = "chandini"

    storage = create_autospec(StorageImplementation)
    presenter = create_autospec(PresenterImplementation)
    oauth2_storage = create_autospec(OAuth2SQLStorage)

    interactor = UserLoginInteractor(
        storage=storage,
        oauth2_storage=oauth2_storage,
        presenter=presenter
        )
    presenter.get_login_response.return_value = user_auth_tokens_dto

    storage.validate_password.side_effect = NotFound
    #act
    with pytest.raises(NotFound):
        interactor.user_login_interactor(
            username=username,
            password=password
            )

    #assert
    storage.validate_username.assert_called_once_with(username=username)
    storage.validate_password.assert_called_once_with(
        username=username,
        password=password
        )
