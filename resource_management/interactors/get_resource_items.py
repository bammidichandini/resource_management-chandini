from typing import List
from resource_management.dtos.dtos import itemdto
from resource_management.exceptions.exceptions import InvalidIdException
from resource_management.interactors.storages.multiple_storage_interface import StorageInterface
from resource_management.interactors.presenters.multiple_presenter_interface import PresenterInterface


class GetResourceItemsInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage


    def get_items_wrapper(
        self, resource_id: int, presenter: PresenterInterface
    ):

        try:
            self.get_items_response(
                resource_id=resource_id,
                presenter=presenter
            )
        except InvalidIdException:
            presenter.raise_invalid_id_exception()


    def get_items_response(
        self, resource_id: int, presenter: PresenterInterface
    ):

        resource_ids = self.storage.get_resources()

        self._validate_resource_ids(
            resource_id=resource_id,
            resource_ids=resource_ids
        )

        item_ids = self.storage.get_item_details(resource_id)
        return item_ids


    def _validate_resource_ids(
        self, resource_id: int, resource_ids: List[int]
    ):
        if resource_id not in resource_ids:
            raise InvalidIdException
