import json
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from django.http import HttpResponse
from resource_management.storages.requests_storage_implementation import StorageImplementation
from resource_management.presenters.authentication_presenter import PresenterImplementation
from resource_management.dtos.dtos import RequestsUpdateDto
from resource_management.exceptions.exceptions import (
    InvalidIdException,
    InvalidDetailsException
    )
from resource_management.constants.exception_messages import (
    INVALID_ID,
    INVALID_DETAILS
    )
from .validator_class import ValidatorClass
from django_swagger_utils.drf_server.exceptions import BadRequest
from resource_management.interactors.update_user_request_interactor \
    import UpdateUserRequestInteractor



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
    request_id = request_data["request_id"]

    access_level = request_data["access_level"]
    duedatetime = request_data["duedatetime"]
    remarks = request_data["remarks"]
    resource_name = request_data["resource_name"]
    item_name = request_data["item_name"]
    access_reason = request_data["access_reason"]

    update_dto = RequestsUpdateDto(
        access_level=access_level,
        duedatetime=duedatetime,
        remarks=remarks,
        resource_name=resource_name,
        item_name=item_name,
        access_reason=access_reason
        )

    storage = StorageImplementation()
    presenter = PresenterImplementation()
    interactor = UpdateUserRequestInteractor(
        storage=storage,
        presenter=presenter
        )
    try:
        interactor.update_user_request_interactor(
            user_id=user.id,
            request_id=request_id,
            update_dto=update_dto
            )
        success_repsonse = "Successfully update the previous details"
        data = json.dumps({'Success Response': success_repsonse})
        response = HttpResponse(data, status=200)
    except InvalidIdException:
        raise BadRequest(*INVALID_ID)
    return response

