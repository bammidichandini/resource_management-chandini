import json
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from django.http import HttpResponse
from resource_management.storages.item_storages_implementation import StorageImplementation
from resource_management.presenters.authentication_presenter import PresenterImplementation
from resource_management.exceptions.exceptions import (
    UserCannotManipulateException,
    InvalidIdException
    )
from resource_management.constants.exception_messages import (
    FORBIDDEN,
    INVALID_ID
    )
from resource_management.exceptions.exceptions import (
    InvalidUserException,
    InvalidPasswordException
    )
from .validator_class import ValidatorClass
from django_swagger_utils.drf_server.exceptions import BadRequest
from resource_management.interactors.delete_items_interactor \
    import DeleteItemsInteractor



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
    item_ids_list = request_data["items_ids_list"]
    storage = StorageImplementation()
    presenter = PresenterImplementation()
    interactor = DeleteItemsInteractor(
        storage=storage,
        presenter=presenter
        )

    interactor.delete_items_interactor(
        user_id=user.id,
        item_ids_list=item_ids_list
        )
    success_repsonse = "Successfully deletes the item_id"
    data = json.dumps({'Success Response': success_repsonse})
    response = HttpResponse(data, status=200)
    return response

