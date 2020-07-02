import pytest
from unittest.mock import create_autospec, patch
from resource_management.exceptions.exceptions \
    import UserCannotManipulateException
from resource_management.interactors.storages.item_storages \
    import StorageInterface
from resource_management.interactors.presenters.presenter_interface \
    import PresenterInterface
from resource_management.interactors.get_resource_items_interactor \
    import GetResourceItemsInteractor


@patch('resource_management.adapters.auth_service.AuthService.get_user_dtos')
@pytest.mark.django_db
def test_get_resource_item(
    get_user_dtos,
    user_dtos,
    item_dto,
    get_item,
    get_req_param
):

    #arrange


    user_id = 1
    param_dto = get_req_param

    get_user_dtos.return_value = user_dtos

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    storage.get_resource_items.return_value = item_dto
    presenter.get_resource_items_response.return_value = get_item

    interactor = GetResourceItemsInteractor(
       storage=storage,
       presenter=presenter
       )

    #act
    actual_dict = interactor.get_resource_items_interactor(
        req_parameter_dto=param_dto,
        user_id=user_id
        )

    #assert
    storage.get_resource_items.assert_called_once_with(
        req_param_dto=param_dto
        )
    presenter.get_resource_items_response.assert_called_once_with(
        items_dto=item_dto
        )
    assert actual_dict[0]["item_name"] == get_item[0]["item_name"]
    assert actual_dict[0]["link"] == get_item[0]["link"]
    assert actual_dict[0]["description"] == get_item[0]["description"]
