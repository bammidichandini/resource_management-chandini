import json
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from django.http import HttpResponse
from resource_management.storages.item_storages_implementation import StorageImplementation
from resource_management.presenters.authentication_presenter import PresenterImplementation
from resource_management.dtos.dtos import ItemDto
from resource_management.exceptions.exceptions import UserCannotManipulateException,InvalidIdException
from resource_management.constants.exception_messages import (
    FORBIDDEN,
    INVALID_ID
    )
from .validator_class import ValidatorClass
from django_swagger_utils.drf_server.exceptions import BadRequest
from resource_management.interactors.update_item_interactor \
    import UpdateItemInteractor



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

    user = kwargs["user"]
    request_data = kwargs['request_data']
    item_id = kwargs['item_id']
    access_level = request_data["access_level"]
    resource_name = request_data["resource_name"]
    item_name = request_data["item_name"]
    link = request_data["link"]
    description = request_data["item_description"]
    item_dto = ItemDto(item_name=item_name,
                        link=link,
                        resource_name=resource_name,
                        description=description,
                        access_level=access_level
                        )
    storage = StorageImplementation()
    presenter = PresenterImplementation()
    interactor = UpdateItemInteractor(
        storage=storage,
        presenter=presenter
        )
    try:
        interactor.update_item_interactor(
            item_id=item_id,
            user_id=user.id,
            item_dto=item_dto
            )
        success_repsonse = "Successfully updated the previous corresonding resource item"
        data = json.dumps({'Success Response': success_repsonse})
        response = HttpResponse(data, status=200)
    except UserCannotManipulateException:
        raise BadRequest(*FORBIDDEN)
    except InvalidIdException:
        raise BadRequest(*INVALID_ID)
    return response

