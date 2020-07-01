import pytest
from unittest.mock  import create_autospec
from resource_management.interactors.storages.resources_storage_interface \
        import StorageInterface
from resource_management.interactors.presenters.presenter_interface \
        import PresenterInterface
from resource_management.interactors.get_user_resources_interactor \
        import GetUserResourcesInteractor


@pytest.mark.django_db
def test_get_user_resource(
    items_dto,
    get_item,
):

    # arrange

    user_id = 1
    expected_response = get_item

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    storage.get_user_resources.return_value = items_dto
    presenter.get_user_resources_response.return_value = get_item

    interactor = GetUserResourcesInteractor(
     storage=storage,
     presenter=presenter
     )

    # act
    actual_response = interactor.get_user_resources_interactor(
        user_id=user_id
        )

    # assert
    storage.get_user_resources.assert_called_once_with(
        user_id=user_id
        )
    presenter.get_user_resources_response.assert_called_once_with(
        items_dto
        )
    assert actual_response[0]["resource_name"] == expected_response[0]["resource_name"]
    assert actual_response[0]["item_name"] == expected_response[0]["item_name"]
    assert actual_response[0]["access_level"] == expected_response[0]["access_level"]
    assert actual_response[0]["link"] == expected_response[0]["link"]
