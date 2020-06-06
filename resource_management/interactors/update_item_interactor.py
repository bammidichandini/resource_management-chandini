from resource_management.interactors.storages.item_storages import StorageInterface
from resource_management.interactors.presenters.presenter_interface import PresenterInterface
from resource_management.exceptions.exceptions import (
    UserCannotManipulateException,
    InvalidDetailsException,
    InvalidIdException
    )
from resource_management.dtos.dtos import ItemDto
from django.core.exceptions import ObjectDoesNotExist


class UpdateItemInteractor:

    def __init__(self, storage: StorageInterface,
                 presenter: PresenterInterface
                 ):
        self.storage = storage
        self.presenter = presenter

    def update_item_interactor(self,
                               item_id: int,
                               item_dto: ItemDto,
                               user_id: int
                               ):
        item_ids_list = [item_id]
        valid_input = self.storage.check_for_valid_input(item_ids_list)

        invalid_input = not valid_input
        if invalid_input:
            self.presenter.raise_invalid_id_exception()

        is_admin = self.storage.is_admin(user_id)

        if is_admin:
                self.storage.update_item(
                    item_id=item_id,
                    item_dto=item_dto,
                    user_id=user_id
                    )
        else:
            self.presenter.raise_user_cannot_manipulate_exception()
