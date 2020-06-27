import json
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from django.http import HttpResponse
from resource_management.storages.item_storages_implementation import StorageImplementation
from resource_management.presenters.authentication_presenter import PresenterImplementation
from resource_management.exceptions.exceptions import UserCannotManipulateException, InvalidIdException
from resource_management.constants.exception_messages import (
    FORBIDDEN,
    INVALID_ID
    )
from django_swagger_utils.drf_server.exceptions import BadRequest
from resource_management.interactors.get_item_accessible_user_interactor \
    import GetUsersForItems



@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    # ---------MOCK IMPLEMENTATION---------

    # try:
    #     from resource_management.views.add_item.tests.test_case_01 \
    #         import TEST_CASE as test_case
    # except ImportError:
    #     from resource_management.views.add_item.tests.test_case_01 \
    #         import test_case

    # from django_swagger_utils.drf_server.utils.server_gen.mock_response \
    #     import mock_response
    # try:
    #     from resource_management.views.add_item.request_response_mocks \
    #         import RESPONSE_200_JSON
    # except ImportError:
    #     RESPONSE_200_JSON = ''
    # response_tuple = mock_response(
    #     app_name="resource_management", test_case=test_case,
    #     operation_name="add_item",
    #     kwargs=kwargs, default_response_body=RESPONSE_200_JSON,
    #     group_name="")
    # return response_tuple[1]

    request_data = kwargs['request_data']
    item_id = request_data['item_id']
    offset = kwargs['request_query_params'].offset
    limit = kwargs['request_query_params'].limit
    storage = StorageImplementation()
    presenter = PresenterImplementation()

    interactor = GetUsersForItems(
        storage=storage,
        presenter=presenter
        )
    response_data = interactor.get_users_for_items_interactor(
            item_id=item_id,
            offset=offset,
            limit=limit
            )
    data = json.dumps({'Users': response_data})
    response = HttpResponse(data, status=200)
    return response
