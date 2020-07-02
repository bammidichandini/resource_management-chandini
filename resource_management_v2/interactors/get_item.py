from typing import List
from resource_management.dtos.dtos import itemdto
from resource_management.exceptions.exceptions import (
    InvalidIdException,
    InvalidItemsException
)
from resource_management.interactors.storages.multiple_storage_interface import StorageInterface
from resource_management.interactors.presenters.multiple_presenter_interface import PresenterInterface


class GetItemInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage


    def get_items_wrapper(
        self, item_ids: List[int], presenter: PresenterInterface,
        offset: int, limit: int
    ):

        try:
            self.get_items_response(
                item_ids=item_ids,
                offset=offset,
                limit=limit,
                presenter=presenter
            )
        except InvalidIdException:
            presenter.raise_invalid_id_exception()


    def get_items_response(
        self, item_ids: List[int], presenter: PresenterInterface,
        offset:int, limit: int
    ):

        item_ids_list = self.storage.get_all_items()

        self.validate_items(item_ids_list, item_ids)

        item_dtos = self.storage.get_item_details(item_ids)
        return item_dtos


    def validate_items(self, item_ids_list: List[int], item_ids: List[int]):
        invalid_items = []
        for item_id in item_ids:
            if item_id not in item_ids_list:
                invalid_items.append(item_id)

        if invalid_items:
            raise InvalidItemsException(invalid_items)
