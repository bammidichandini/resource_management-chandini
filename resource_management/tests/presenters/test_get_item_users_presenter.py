import pytest
from resource_management.presenters.authentication_presenter import PresenterImplementation


@pytest.mark.django_db
def test_get_item_users(get_request_response,
                        user_dtos,
                        request_dto
                        ):

    # arrange

    input = user_dtos
    count = 3

    expected_response = get_request_response

    presenter = PresenterImplementation()

    # act
    actual_response = presenter.get_user_for_items_response(
        user_dtos=input,
        request_dto=request_dto,
        count=count
        )

    # assert
    assert actual_response["users"][0]["person_name"] == expected_response["users"][0]["person_name"]
    assert actual_response["users"][0]["department"] == expected_response["users"][0]["department"]
    assert actual_response["users"][0]["job_role"] == expected_response["users"][0]["job_role"]
    assert actual_response["users"][0]["access_level"] == expected_response["users"][0]["access_level"]
    # assert actual_response == expected_response
