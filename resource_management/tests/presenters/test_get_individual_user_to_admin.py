import pytest
from resource_management.presenters.authentication_presenter import PresenterImplementation


@pytest.mark.django_db
def test_get_individual_user_details(
    get_user_requests_response,
    user_requests_dto,
    user_dtos
):

    # arrange

    expected_response = get_user_requests_response
    presenter = PresenterImplementation()

    # act
    actual_response = presenter.get_individual_user_details_to_admin_response(
        user_requests_dto=user_requests_dto,
        user_dto=user_dtos
        )

    # assert
    assert expected_response == actual_response
