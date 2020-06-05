import json
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from django.http import HttpResponse
from resource_management.storages.user_profile_details_storage import StorageImplementation
from resource_management.presenters.authentication_presenter import PresenterImplementation
from resource_management.dtos.dtos import UpdateProfileDto
from resource_management.exceptions.exceptions import InvalidDetailsException
from resource_management.constants.exception_messages import (
    INVALID_DETAILS
    )
from .validator_class import ValidatorClass
from django_swagger_utils.drf_server.exceptions import BadRequest
from resource_management.interactors.update_user_profile_interactor \
    import UpdateUserProfileInteractor



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
    name = request_data["name"]
    email = request_data["email"]
    gender = request_data["gender"]
    job_role = request_data["job_role"]
    department = request_data["department"]

    user_profile_dto = UpdateProfileDto(
        name=name,
        email=email,
        gender=gender,
        job_role=job_role,
        department=department
        )

    storage = StorageImplementation()
    presenter = PresenterImplementation()
    interactor = UpdateUserProfileInteractor(
        storage=storage,
        presenter=presenter
        )
    try:
        interactor.update_user_details_interactor(
            user_id=user.id,
            user_profile_dto=user_profile_dto
            )
        success_repsonse = "Successfully updated the previous details"
        data = json.dumps({'Success Response': success_repsonse})
        response = HttpResponse(data, status=200)
    except InvalidDetailsException:
        raise BadRequest(*INVALID_DETAILS)
    return response

