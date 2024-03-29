import json
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from django.http import HttpResponse
from resource_management.storages.user_profile_details_storage import StorageImplementation
from resource_management.presenters.authentication_presenter import PresenterImplementation
from django_swagger_utils.drf_server.exceptions import BadRequest
from resource_management.interactors.update_password_interactor \
    import UpdatePasswordInteractor


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    # ---------MOCK IMPLEMENTATION---------

    # try:
    #     from resource_management.views.change_user_password.tests.test_case_01 \
    #         import TEST_CASE as test_case
    # except ImportError:
    #     from resource_management.views.change_user_password.tests.test_case_01 \
    #         import test_case

    # from django_swagger_utils.drf_server.utils.server_gen.mock_response \
    #     import mock_response
    # try:
    #     from resource_management.views.change_user_password.request_response_mocks \
    #         import RESPONSE_200_JSON
    # except ImportError:
    #     RESPONSE_200_JSON = ''
    # response_tuple = mock_response(
    #     app_name="resource_management", test_case=test_case,
    #     operation_name="change_user_password",
    #     kwargs=kwargs, default_response_body=RESPONSE_200_JSON,
    #     group_name="")
    # return response_tuple[1]
    user = kwargs["user"]
    request_data = kwargs['request_data']
    password = request_data["password"]

    storage = StorageImplementation()
    presenter = PresenterImplementation()
    interactor = UpdatePasswordInteractor(
        storage=storage,
        presenter=presenter
        )

    interactor.update_password_interactor(
        user_id=user.id,
        password=password
        )
    success_repsonse = "Successfully updated previous password"
    data = json.dumps({'Success Response': success_repsonse})
    response = HttpResponse(data, status=200)

    return response





