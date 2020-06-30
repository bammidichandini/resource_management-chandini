from typing import List
from resource_management.exceptions.exceptions import InvalidIdException
from resource_management.adapters import service_adapter
from resource_management.interactors.storages.item_storages \
    import StorageInterface
from resource_management.interactors.presenters.presenter_interface \
    import PresenterInterface


class GetUsersForItems:

    def __init__(
        self,
        storage: StorageInterface,
        presenter: PresenterInterface
    ):

        self.storage = storage
        self.presenter = presenter


    def get_users_for_items_interactor(
        self,
        item_id: int,
        offset: int,
        limit: int
    ):

        item_ids_list = [limit]

        valid_input = self.storage.check_for_valid_input(item_ids_list)

        valid_offset = self.storage.check_for_valid_offset(offset)

        invalid_offset = not valid_offset

        invalid_input = not valid_input

        if invalid_input or invalid_offset:
            self.presenter.raise_invalid_id_exception()

        item_ids = self.storage.get_item_ids()
        self._validate_item_ids(item_ids, item_id)

        user_ids = self.storage.get_user_ids(
            item_id=item_id, offset=offset, limit=limit
        )

        service_adapter_obj = service_adapter.get_service_adapter()
        user_dtos = service_adapter_obj.auth_service.get_user_dtos(user_ids)

        count = self.storage.get_user_items_count(
            item_id=item_id, offset=offset, limit=limit
        )

        list_of_user_dto = self.storage.get_users_for_items(
                item_id=item_id,
                offset=offset,
                limit=limit
                )

        response = self.presenter.get_user_for_items_response(
            request_dto=list_of_user_dto,
            count=count,
            user_dtos=user_dtos
            )

        return response

    def _validate_item_ids(self, item_ids: List[int], item_id: int):
        if item_id not in item_ids:
            self.presenter.raise_invalid_id_exception()
