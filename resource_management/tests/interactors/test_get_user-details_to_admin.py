import pytest
from unittest.mock import create_autospec, patch
from resource_management.interactors.storages.user_details_to_admin_storages \
    import StorageInterface
from resource_management.interactors.presenters.presenter_interface \
    import PresenterInterface
from resource_management.interactors.get_user_details_to_admin_interactor \
    import GetUserDetailsToAdminInteractor


@pytest.mark.django_db
@patch('resource_management.adapters.auth_service.AuthService.get_all_user_dtos')
def test_get_user_details(
    get_all_user_dtos,
    user_details,
    user_response
    ):

    # arrange

    expected_response = user_response

    get_all_user_dtos.return_value = user_details

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    presenter.get_user_details_to_admin_response.return_value = \
            user_response

    interactor = GetUserDetailsToAdminInteractor(
        storage=storage,
        presenter=presenter
        )

    # act

    actual_response = interactor.get_user_details_to_admin_interactor()

    # assert
    presenter.get_user_details_to_admin_response.assert_called_once_with(
        user_details
        )
    assert actual_response[0]["person_name"] == expected_response[0]["person_name"]
    assert actual_response[0]["job_role"] == expected_response[0]["job_role"]
    assert actual_response[0]["department"] == expected_response[0]["department"]
    assert actual_response[0]["profile_pic"] == expected_response[0]["profile_pic"]
