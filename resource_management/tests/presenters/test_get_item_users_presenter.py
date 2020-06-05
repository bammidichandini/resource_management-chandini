import pytest
from resource_management.presenters.authentication_presenter import PresenterImplementation


@pytest.mark.django_db
def test_get_item_users(get_item_users_response,
                        get_item_users
                        ):

    # arrange

    input = get_item_users
    expected_response = get_item_users_response

    presenter = PresenterImplementation()

    # act
    actual_response = presenter.get_user_for_items_response(
        input
        )

    # assert
    assert actual_response[0]["person_name"] == expected_response[0]["person_name"]
    assert actual_response[0]["department"] == expected_response[0]["department"]
    assert actual_response[0]["job_role"] == expected_response[0]["job_role"]
    assert actual_response[0]["access_level"] == expected_response[0]["access_level"]
