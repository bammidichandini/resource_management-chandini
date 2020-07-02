from typing import List
from resource_management.interactors.storages.item_storages \
    import StorageInterface
from resource_management.interactors.presenters.presenter_interface \
    import PresenterInterface
from resource_management.adapters import service_adapter
from resource_management.dtos.dtos import ItemDto


class UpdateItemInteractor:

    def __init__(
        self,
        storage: StorageInterface,
        presenter: PresenterInterface
    ):

        self.storage = storage
        self.presenter = presenter

    def update_item_interactor(
        self,
        item_id: int,
        item_dto: ItemDto,
        user_id: int
    ):
        item_ids = self.storage.get_item_ids()
        self._validate_item_ids(item_ids, item_id)

        is_admin = self._check_whether_user_is_an_admin_or_not(user_id)

        if is_admin:
                self.storage.update_item(
                    item_id=item_id,
                    item_dto=item_dto,
                    user_id=user_id
                )
        else:
            self.presenter.raise_user_cannot_manipulate_exception()

    def _check_whether_user_is_an_admin_or_not(self, user_id: int):
        service_adapter_obj = service_adapter.get_service_adapter()
        user_dtos = service_adapter_obj.auth_service.get_user_dtos([user_id])
        is_admin = user_dtos[0].is_admin
        return is_admin

    def _validate_item_ids(self, item_ids: List[int], item_id: int):
        if item_id not in item_ids:
            self.presenter.raise_invalid_id_exception()
