from typing import List
from resource_management.dtos.dtos import ItemDto
from django.core.exceptions import ObjectDoesNotExist
from resource_management.exceptions.exceptions import InvalidIdException
from resource_management.adapters import service_adapter
from resource_management.interactors.storages.item_storages \
    import StorageInterface
from resource_management.interactors.presenters.presenter_interface \
    import PresenterInterface


class DeleteItemsInteractor:

    def __init__(
        self,
        storage: StorageInterface,
        presenter: PresenterInterface
    ):
        self.storage = storage
        self.presenter = presenter

    def delete_items_interactor(
        self,
        item_ids_list: List[int],
        user_id: int
    ):
        item_ids = self.storage.get_item_ids()
        self._validate_item_ids(item_ids, item_ids_list)
        is_admin = self._check_whether_user_is_an_admin_or_not(user_id)

        if is_admin:
                self.storage.delete_items(
                    user_id=user_id,
                    item_ids_list=item_ids_list
                )
        else:
            self.presenter.raise_user_cannot_manipulate_exception()


    def _check_whether_user_is_an_admin_or_not(self, user_id: int):
        service_adapter_obj = service_adapter.get_service_adapter()
        user_dtos = service_adapter_obj.auth_service.get_user_dtos([user_id])
        is_admin = user_dtos[0].is_admin
        return is_admin

    def _validate_item_ids(self, item_ids: List[int], item_ids_list: List[int]):
        invalid_ids = []
        for item_id in item_ids_list:
            if not item_id in item_ids:
                invalid_ids.append(item_id)

        if invalid_ids:
            self.presenter.raise_invalid_id_exception()
