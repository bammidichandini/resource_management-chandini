from user_authentication_app.models import User
from typing import List
from user_authentication_app.tests.factories import UserFactory
from  user_authentication_app.interactors.storage_interfaces.dtos import UserDTO
from common.oauth_user_auth_tokens_service import OAuthUserAuthTokensService as oauthservice


def get_user_dtos_mock(mocker, user_ids: List[int]):
    mock = mocker.patch(
        'common.oauth_user_auth_tokens_service.OAuthUserAuthTokensService.create_user_auth_tokens'
    )
    return mock

