import json
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from django.http import HttpResponse
from resource_management.storages.user_details_to_admin_storages \
    import StorageImplementation
from resource_management.presenters.authentication_presenter \
    import PresenterImplementation
from .validator_class import ValidatorClass
from django_swagger_utils.drf_server.exceptions import BadRequest
from resource_management.interactors.get_user_details_to_admin_interactor \
    import GetUserDetailsToAdminInteractor



@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    # ---------MOCK IMPLEMENTATION---------

    # try:
    #     from resource_management.views.create_resource.tests.test_case_01 \
    #         import TEST_CASE as test_case
    # except ImportError:
    #     from resource_management.views.create_resource.tests.test_case_01 \
    #         import test_case

    # from django_swagger_utils.drf_server.utils.server_gen.mock_response \
    #     import mock_response
    # try:
    #     from resource_management.views.create_resource.request_response_mocks \
    #         import RESPONSE_200_JSON
    # except ImportError:
    #     RESPONSE_200_JSON = ''
    # response_tuple = mock_response(
    #     app_name="resource_management", test_case=test_case,
    #     operation_name="create_resource",
    #     kwargs=kwargs, default_response_body=RESPONSE_200_JSON,
    #     group_name="")
    # return response_tuple[1]


    storage = StorageImplementation()
    presenter = PresenterImplementation()
    interactor = GetUserDetailsToAdminInteractor(
        storage=storage,
        presenter=presenter
        )
    users_data = interactor.get_user_details_to_admin_interactor()
    data = json.dumps({'Users_data': users_data})
    response = HttpResponse(data, status=200)
    return response

