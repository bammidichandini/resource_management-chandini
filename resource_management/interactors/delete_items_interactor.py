from typing import List
from resource_management.dtos.dtos import ItemDto
from resource_management.interactors.storages.item_storages import StorageInterface
from resource_management.interactors.presenters.presenter_interface import PresenterInterface
from resource_management.exceptions.exceptions import (
    UserCannotManipulateException,
    InvalidIdException
    )


class DeleteItemsInteractor:

    def __init__(self, storage: StorageInterface,
                 presenter: PresenterInterface
                ):
        self.storage = storage
        self.presenter = presenter

    def delete_items_interactor(self,
                               item_ids_list: List[int],
                               user_id: int
                               ):
        valid_input = self.storage.check_for_valid_input(item_ids_list)

        invalid_input = not valid_input
        if invalid_input:
            self.presenter.raise_invalid_id_exception()
        is_admin = self.storage.is_admin(user_id)

        if is_admin:
            self.storage.delete_items(
                user_id=user_id,
                item_ids_list=item_ids_list
                )
        else:
            self.presenter.raise_user_cannot_manipulate_exception()

