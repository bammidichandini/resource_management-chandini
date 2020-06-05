from unittest.mock import create_autospec
import pytest
from resource_management.interactors.storages.requests_storage_interface  \
    import StorageInterface
from resource_management.interactors.presenters.presenter_interface \
    import PresenterInterface
from resource_management.interactors.get_individual_user_to_admin_interactor \
    import GetIndividualUserDetailsToAdmin


@pytest.mark.django_db
def test_get_individual_user(
    create_users1,
    get_user_requests_response,
    user_requests_dto
):

    # arrange

    user_id = 2
    expected_response = get_user_requests_response

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    storage.get_individual_user_details_to_admin.return_value = \
            user_requests_dto
    presenter.get_individual_user_details_to_admin_response.return_value = \
        expected_response

    interactor = GetIndividualUserDetailsToAdmin(
        storage=storage,
        presenter=presenter
        )

    # act
    actual_response = interactor.get_individual_user_details_to_admin_interactor(
        user_id=user_id
        )

    # assert
    storage.get_individual_user_details_to_admin.assert_called_once_with(
        user_id=user_id
        )
    presenter.get_individual_user_details_to_admin_response.\
            assert_called_once_with(
                user_requests_dto
                )
    assert actual_response[0]["person_name"] == expected_response[0]["person_name"]
    assert actual_response[0]["department"] == expected_response[0]["department"]
    assert actual_response[0]["job_role"] == expected_response[0]["job_role"]
    assert actual_response[0]["profile_pic"] == expected_response[0]["profile_pic"]
    assert actual_response[0]["resource_name"] == expected_response[0]["resource_name"]
    assert actual_response[0]["item_name"] == expected_response[0]["item_name"]
    assert actual_response[0]["access_level"] == expected_response[0]["access_level"]
