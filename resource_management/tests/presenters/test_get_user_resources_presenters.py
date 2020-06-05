import pytest
from resource_management.presenters.authentication_presenter \
    import PresenterImplementation


@pytest.mark.django_db
def test_get_user_resources(
    item_dto,
    get_resource_items_response
):

    # arrange
    user_id = 1
    expected_dto = get_resource_items_response

    presenter = PresenterImplementation()

    # act
    actual_dto = presenter.get_user_resources_response(
        item_dto
        )

    # assert
    assert actual_dto[0]["resource_name"] == expected_dto[0]["resource_name"]
    assert actual_dto[0]["item_name"] == expected_dto[0]["item_name"]
    assert actual_dto[0]["access_level"] == expected_dto[0]["access_level"]
    assert actual_dto[0]["link"] == expected_dto[0]["link"]

