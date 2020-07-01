import pytest
from resource_management.presenters.authentication_presenter import PresenterImplementation


@pytest.mark.django_db
def test_get_user_details(
    user_response,
    user_details
):

    # arrange

    expected_response = user_response
    presenter = PresenterImplementation()

    # act
    response = presenter.get_user_details_to_admin_response(user_details)

    # assert

    assert response[0]["person_name"] == expected_response[0]["person_name"]
    assert response[0]["department"] == expected_response[0]["department"]
    assert response[0]["job_role"] == expected_response[0]["job_role"]
    assert response[0]["profile_pic"] == expected_response[0]["profile_pic"]
