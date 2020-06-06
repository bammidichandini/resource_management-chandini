from resource_management.interactors.storages.item_storages import StorageInterface
from resource_management.exceptions.exceptions import InvalidIdException
from resource_management.interactors.presenters.presenter_interface import PresenterInterface


class GetUsersForItems:

    def __init__(self, storage: StorageInterface,
                 presenter: PresenterInterface
                ):
        self.storage = storage
        self.presenter = presenter

    def get_users_for_items_interactor(self,
                                       item_id: int,
                                       offset: int,
                                       limit: int
                                       ):
        item_ids_list = [item_id,limit]
        valid_input = self.storage.check_for_valid_input(item_ids_list)

        valid_offset = self.storage.check_for_valid_offset(offset)

        invalid_offset = not valid_offset

        invalid_input = not valid_input

        if invalid_input or invalid_offset:
            self.presenter.raise_invalid_id_exception()

        list_of_user_dto = self.storage.get_users_for_items(
                item_id=item_id,
                offset=offset,
                limit=limit
                )

        response = self.presenter.get_user_for_items_response(
            user_dto=list_of_user_dto
            )

        return response