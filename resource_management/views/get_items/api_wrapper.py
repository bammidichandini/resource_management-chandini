import json
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from django.http import HttpResponse
from resource_management.dtos.dtos import ResourceItemParametersDto
from resource_management.storages.item_storages_implementation import StorageImplementation
from resource_management.presenters.authentication_presenter import PresenterImplementation
from resource_management.exceptions.exceptions import UserCannotManipulateException, InvalidIdException
from resource_management.dtos.dtos import ItemDto
from resource_management.constants.exception_messages import (
    FORBIDDEN,
    INVALID_ID
    )
from django_swagger_utils.drf_server.exceptions import BadRequest
from resource_management.interactors.get_resource_items_interactor \
    import GetResourceItemsInteractor


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    # ---------MOCK IMPLEMENTATION---------

    # try:
    #     from resource_management.views.get_items.tests.test_case_01 \
    #         import TEST_CASE as test_case
    # except ImportError:
    #     from resource_management.views.get_items.tests.test_case_01 \
    #         import test_case

    # from django_swagger_utils.drf_server.utils.server_gen.mock_response \
    #     import mock_response
    # try:
    #     from resource_management.views.get_items.request_response_mocks \
    #         import RESPONSE_200_JSON
    # except ImportError:
    #     RESPONSE_200_JSON = ''
    # response_tuple = mock_response(
    #     app_name="resource_management", test_case=test_case,
    #     operation_name="get_items",
    #     kwargs=kwargs, default_response_body=RESPONSE_200_JSON,
    #     group_name="")
    # return response_tuple[1]
    user = kwargs['user']
    offset = kwargs['request_query_params'].offset
    limit = kwargs['request_query_params'].limit
    resource_id = kwargs['resource_id']
    storage = StorageImplementation()
    presenter = PresenterImplementation()
    interactor = GetResourceItemsInteractor(
        storage=storage,
        presenter=presenter
        )
    req_param_dto = ResourceItemParametersDto(
        resource_id=resource_id,
        offset=offset,
        limit=limit
        )
    try:
        resources_item_dict = interactor.get_resource_items_interactor(
            req_parameter_dto=req_param_dto,
            user_id=user.id
            )
        data = json.dumps({'Resources': resources_item_dict})
        response = HttpResponse(data, status=200)
    except InvalidIdException:
        raise BadRequest(*INVALID_ID)
    except UserCannotManipulateException:
        raise BadRequest(*FORBIDDEN)
    return response
