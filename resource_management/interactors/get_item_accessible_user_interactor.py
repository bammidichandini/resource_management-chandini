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


        valid_input = self._check_for_valid_limit(limit)

        valid_offset = self._check_for_valid_offset(offset)

        invalid_offset = not valid_offset

        invalid_input = not valid_input

        if invalid_input or invalid_offset:
            self.presenter.raise_invalid_input_exception()

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

    def _check_for_valid_limit(self, limit) -> bool:
        if limit <= 0 :
            return False
        return True

    def _check_for_valid_offset(self, offset):
        if offset < 0:
            return False
        return True
