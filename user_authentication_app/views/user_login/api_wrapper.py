from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
import json
from django.http import HttpResponse
from .validator_class import ValidatorClass
from user_authentication_app.interactors.user_login import UserLoginInteractor
# from user_authentication_app.presenters.authentication_presenter import PresenterImplementation
from user_authentication_app.storages.authentication_storage import StorageImplementation
from common.oauth2_storage import OAuth2SQLStorage


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    # ---------MOCK IMPLEMENTATION---------

    # try:
    #     from user_authentication_app.views.user_login.tests.test_case_01 \
    #         import TEST_CASE as test_case
    # except ImportError:
    #     from user_authentication_app.views.user_login.tests.test_case_01 \
    #         import test_case

    # from django_swagger_utils.drf_server.utils.server_gen.mock_response \
    #     import mock_response
    # try:
    #     from user_authentication_app.views.user_login.request_response_mocks \
    #         import RESPONSE_200_JSON
    # except ImportError:
    #     RESPONSE_200_JSON = ''
    # response_tuple = mock_response(
    #     app_name="user_authentication_app", test_case=test_case,
    #     operation_name="user_login",
    #     kwargs=kwargs, default_response_body=RESPONSE_200_JSON,
    #     group_name="")
    # return response_tuple
    request_data = kwargs['request_data']
    username = request_data['username']
    password = request_data['password']
    storage = StorageImplementation()
    # presenter = PresenterImplementation()
    oauth2_storage = OAuth2SQLStorage()
    interactor = UserLoginInteractor(
        storage=storage,
        oauth2_storage=oauth2_storage
        )

    AccessToken = interactor.user_login_interactor(
        username=username,
        password=password
        )
    data = json.dumps({'AccessToken': AccessToken})
    response = HttpResponse(data, status=200)
    return response
