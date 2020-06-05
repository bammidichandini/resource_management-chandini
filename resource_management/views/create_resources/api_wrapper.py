import json
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from django.http import HttpResponse
from resource_management.storages.authentication_storage import StorageImplementation
from resource_management.presenters.authentication_presenter import PresenterImplementation
from resource_management.exceptions.exceptions import UserCannotManipulateException
from resource_management.dtos.dtos import ResourceDto
from resource_management.constants.exception_messages import (
    FORBIDDEN
    )
from resource_management.exceptions.exceptions import (
    InvalidUserException,
    InvalidPasswordException
    )
from .validator_class import ValidatorClass
from django_swagger_utils.drf_server.exceptions import BadRequest
from resource_management.interactors.create_resources_interactor \
    import CreateResourceInteractor



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
    image_url = request_data["image_url"]
    resource_name = request_data["name"]
    item_name = request_data["item_name"]
    link = request_data["link"]
    description = request_data["description"]

    resource_dto = ResourceDto(
            image_url=image_url,
            name=resource_name,
            item_name=item_name,
            link=link,
            description=description
        )
    storage = StorageImplementation()
    presenter = PresenterImplementation()
    interactor = CreateResourceInteractor(
        storage=storage,
        presenter=presenter
        )
    try:
        interactor.create_resource_interactor(
            resource_dto=resource_dto,
            user_id=user.id
            )
        success_repsonse = "Successfully created a new resource"
        data = json.dumps({'Success Response': success_repsonse})
        response = HttpResponse(data, status=200)
    except UserCannotManipulateException:
        raise BadRequest(*FORBIDDEN)
    return response

