import pytest
from unittest.mock import create_autospec
from user_auth.storages.authentication_storage import StorageImplementation
from user_auth.presenters.authentication_presenter import PresenterImplementation
from user_auth.interactors.user_signup import UserSignUpInteractor
# from user_auth.interactors.status_interactor import StatusInteractor
from user_auth.exceptions.exceptions import InvalidIdException
from common.oauth_user_auth_tokens_service import OAuthUserAuthTokensService
from user_auth.exceptions.exceptions import UserAlreadyExistedException
from common.oauth2_storage import OAuth2SQLStorage
from django_swagger_utils.drf_server.exceptions import NotFound


def test_user_signup(
        user_auth_tokens_dto,
        access_dto,
        refresh_token_dto,
        application_dto
    ):

    # arrange

    user_id =  3
    username = "bakka vamsi"
    password = "bakka vamsi"

    storage = create_autospec(StorageImplementation)
    presenter = create_autospec(PresenterImplementation)
    oauth2_storage = create_autospec(OAuth2SQLStorage)

    interactor = UserSignUpInteractor(
        storage=storage,
        oauth2_storage=oauth2_storage,
        presenter=presenter
        )

    storage.is_user_exists.return_value = False
    presenter.get_signup_response.return_value = user_auth_tokens_dto

    storage.create_a_new_user.return_value = user_id
    oauth2_storage.get_or_create_default_application.return_value \
       = application_dto,True
    oauth2_storage.create_access_token.return_value = access_dto
    oauth2_storage.create_refresh_token.return_value = refresh_token_dto

    #act
    access_token_obj = interactor.user_signup_interactor(
        username=username,
        password=password
        )

    #assert
    assert access_token_obj.user_id == user_auth_tokens_dto.user_id
    assert access_token_obj.access_token == user_auth_tokens_dto.access_token
    assert access_token_obj.refresh_token == user_auth_tokens_dto.refresh_token
    assert access_token_obj.expires_in == user_auth_tokens_dto.expires_in
    storage.is_user_exists.assert_called_once_with(username=username)
    storage.create_a_new_user.assert_called_once_with(
        username=username,
        password=password
        )

def test_user_signup_with_existed_user(user_auth_tokens_dto,
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

    interactor = UserSignUpInteractor(
        storage=storage,
        oauth2_storage=oauth2_storage,
        presenter=presenter
        )

    storage.is_user_exists.return_value = True
    presenter.get_signup_response.return_value = user_auth_tokens_dto

    presenter.raise_user_already_existed_exception.side_effect = \
                UserAlreadyExistedException

    #act
    with pytest.raises(UserAlreadyExistedException):
        interactor.user_signup_interactor(
            username=username,
            password=password
            )

    #assert
    storage.is_user_exists.assert_called_once_with(username=username)
    presenter.raise_user_already_existed_exception.assert_called_once()



# @pytest.mark.django_db
# def test_user_signup(create_users1):

#     # arrange

#     username = "chandini"
#     password = "chandini"

#     storage = create_autospec(StorageInterface)
#     presenter = create_autospec(PresenterInterface)

#     storage.is_user_exists.return_value = False

#     interactor = UserSignUpInteractor(
#         storage=storage,
#         presenter=presenter
#         )

#     # act
#     interactor.user_signup_interactor(
#         username=username,
#         password=password
#         )

#     # assert

#     User.objects.filter(username=username).exists()
#     User.objects.get(username=username)
#     storage.is_user_exists.assert_called_once_with(username)
#     storage.create_a_new_user.assert_called_once_with(
#         username=username,
#         password=password
#         )


# @pytest.mark.django_db
# def test_user_signup_with_existed_user(create_users1):

#     # arrange

#     username = "chandini"
#     password = "chandini"

#     storage = create_autospec(StorageInterface)
#     presenter = create_autospec(PresenterInterface)

#     storage.is_user_exists.return_value = True
#     presenter.raise_user_already_existed_exception.side_effect = \
#         UserAlreadyExistedException

#     interactor = UserSignUpInteractor(
#         storage=storage,
#         presenter=presenter
#         )

#     # act
#     with pytest.raises(UserAlreadyExistedException):
#         interactor.user_signup_interactor(
#             username=username,
#             password=password
#             )

#     # assert

#     storage.is_user_exists.assert_called_once_with(username)
#     presenter.raise_user_already_existed_exception.assert_called_once()