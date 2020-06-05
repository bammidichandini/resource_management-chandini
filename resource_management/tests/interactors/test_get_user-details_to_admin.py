import pytest
from unittest.mock import create_autospec
from resource_management.interactors.storages.user_details_to_admin_storages \
    import StorageInterface
from resource_management.interactors.presenters.presenter_interface \
    import PresenterInterface
from resource_management.interactors.get_user_details_to_admin_interactor \
    import GetUserDetailsToAdminInteractor


@pytest.mark.django_db
def test_get_user_details(user_details,
                          create_users1,
                          user_response
                          ):

    # arrange

    expected_response = user_response
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    storage.get_user_details_to_admin.return_value = user_details
    presenter.get_user_details_to_admin_response.return_value = \
            user_response

    interactor = GetUserDetailsToAdminInteractor(
        storage=storage,
        presenter=presenter
        )

    # act

    actual_response = interactor.get_user_details_to_admin_interactor()

    # assert
    storage.get_user_details_to_admin.assert_called_once()
    presenter.get_user_details_to_admin_response.assert_called_once_with(
        user_details
        )
    assert actual_response[0]["person_name"] == expected_response[0]["person_name"]
    assert actual_response[0]["job_role"] == expected_response[0]["job_role"]
    assert actual_response[0]["department"] == expected_response[0]["department"]
    assert actual_response[0]["url"] == expected_response[0]["url"]
