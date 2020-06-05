import json
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from django.http import HttpResponse
from resource_management.storages.authentication_storage import StorageImplementation
from resource_management.presenters.authentication_presenter import PresenterImplementation
from resource_management.constants.exception_messages import (
    INVALID_PASSWORD,
    INVALID_USER
    )
from resource_management.exceptions.exceptions import (
    InvalidUserException,
    InvalidPasswordException
    )
from common.oauth2_storage import OAuth2SQLStorage
from django_swagger_utils.drf_server.exceptions import BadRequest
from resource_management.interactors.user_login_interactor import UserLoginInteractor


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    # ---------MOCK IMPLEMENTATION---------

    # try:
    #     from resource_management.views.login.tests.test_case_01 \
    #         import TEST_CASE as test_case
    # except ImportError:
    #     from resource_management.views.login.tests.test_case_01 \
    #         import test_case

    # from django_swagger_utils.drf_server.utils.server_gen.mock_response \
    #     import mock_response
    # try:
    #     from resource_management.views.login.request_response_mocks \
    #         import RESPONSE_200_JSON
    # except ImportError:
    #     RESPONSE_200_JSON = ''
    # response_tuple = mock_response(
    #     app_name="resource_management", test_case=test_case,
    #     operation_name="login",
    #     kwargs=kwargs, default_response_body=RESPONSE_200_JSON,
    #     group_name="")
    # return response_tuple[1]
    request_data = kwargs['request_data']
    username = request_data['username']
    password = request_data['password']
    storage = StorageImplementation()
    presenter = PresenterImplementation()
    oauth2_storage = OAuth2SQLStorage()
    interactor = UserLoginInteractor(
        storage=storage,
        oauth2_storage=oauth2_storage,
        presenter=presenter
        )
    try:
        AccessToken = interactor.user_login_interactor(
            username=username,
            password=password
            )
        data = json.dumps({'AccessToken': AccessToken})
        response = HttpResponse(data, status=200)
    except InvalidUserException:
        raise BadRequest(*INVALID_USER)
    except InvalidPasswordException:
        raise BadRequest(*INVALID_PASSWORD)
    return response
