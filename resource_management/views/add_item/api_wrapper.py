import json
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from django.http import HttpResponse
from resource_management.storages.item_storages_implementation import StorageImplementation
from resource_management.presenters.authentication_presenter import PresenterImplementation
from resource_management.exceptions.exceptions import UserCannotManipulateException
from resource_management.dtos.dtos import ItemDto
from resource_management.constants.exception_messages import (
    FORBIDDEN
    )
from django_swagger_utils.drf_server.exceptions import BadRequest
from resource_management.interactors.create_resource_item_interactor \
    import CreateResourceItemInteractor



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
    user = kwargs["user"]
    request_data = kwargs['request_data']
    resource_name = request_data["resource_name"]
    item_name = request_data["item_name"]
    link = request_data["link"]
    description = request_data["item_description"]

    item_dto = ItemDto(
            resource_name=resource_name,
            item_name=item_name,
            link=link,
            description=description
        )

    storage = StorageImplementation()
    presenter = PresenterImplementation()
    interactor = CreateResourceItemInteractor(
        storage=storage,
        presenter=presenter
        )
    try:
        interactor.create_item_interactor(
            item_dto=item_dto,
            user_id=user.id
            )
        success_repsonse = "Successfully created a new resource"
        data = json.dumps({'Success Response': success_repsonse})
        response = HttpResponse(data, status=200)
    except UserCannotManipulateException:
        raise BadRequest(*FORBIDDEN)
    return response
