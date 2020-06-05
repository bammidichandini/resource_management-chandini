import pytest
from resource_management.presenters.authentication_presenter import PresenterImplementation


@pytest.mark.django_db
def test_get_user_requests(
  get_user_requests_dto,
  get_user_requests_dto_response
):

    # arrange

    expected_response = get_user_requests_dto_response
    input = get_user_requests_dto

    presenter = PresenterImplementation()

    # act
    response = presenter.get_user_requests_response(input)

    # assert
    assert expected_response[0]["resource_name"] == response[0]["resource_name"]
    assert expected_response[0]["item_name"] == response[0]["item_name"]
    assert expected_response[0]["access_level"] == response[0]["access_level"]
    assert expected_response[0]["status"] == response[0]["status"]

