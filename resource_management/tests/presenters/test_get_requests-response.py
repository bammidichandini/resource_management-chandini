import pytest
from resource_management.presenters.authentication_presenter import PresenterImplementation


@pytest.mark.django_db
def test_get_request_presenter(
    requests,
    get_requests
    ):

    # arrange

    expected_response = requests
    input = get_requests

    presenter = PresenterImplementation()

    # act

    actual_response = presenter.get_requests_response(input)

    # assert

    assert actual_response[0]["name"] == expected_response[0]["name"]
    assert actual_response[0]["access_level"] == \
            expected_response[0]["access_level"]
    assert actual_response[0]["duedatetime"] == \
            expected_response[0]["duedatetime"]
    assert actual_response[0]["item_name"] == \
            expected_response[0]["item_name"]
