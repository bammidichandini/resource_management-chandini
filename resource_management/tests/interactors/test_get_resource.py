import pytest
from unittest.mock import create_autospec
from resource_management.exceptions.exceptions import UserCannotManipulateException
from resource_management.interactors.storages.resources_storage_interface import StorageInterface
from resource_management.interactors.presenters.presenter_interface import PresenterInterface
from resource_management.interactors.get_resource_interactor import GetResourcesInteractor


def test_get_resource(resource_dto,
                      get_resource):

    #arrange

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    storage.get_resources.return_value = resource_dto
    presenter.get_resources_response.return_value = get_resource

    interactor = GetResourcesInteractor(
       storage=storage,
       presenter=presenter
       )

    #act
    actual_dict = interactor.get_resources_interactor()

    #assert
    storage.get_resources.assert_called_once()
    presenter.get_resources_response.assert_called_once_with(
        resources_dto_list=resource_dto
        )
    assert actual_dict[0] == get_resource[0]
