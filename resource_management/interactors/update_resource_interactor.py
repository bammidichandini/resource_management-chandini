from typing import List
from resource_management.dtos.dtos import ResourceDto
from resource_management.interactors.storages.resources_storage_interface \
    import StorageInterface
from resource_management.interactors.presenters.presenter_interface \
    import PresenterInterface
from resource_management.adapters import service_adapter


class UpdateResourceInteractor:

    def __init__(
        self,
        storage: StorageInterface,
        presenter: PresenterInterface
    ):

        self.storage = storage
        self.presenter = presenter

    def update_resource_interactor(
        self,
        resource_id: int,
        resource_dto: ResourceDto,
        user_id: int
    ):

        # ids_list = [resource_id]
        # valid_input = self.storage.check_for_valid_input(ids_list)

        # invalid_input = not valid_input

        # if invalid_input:
        #     self.presenter.raise_invalid_id_exception()
        resource_ids = self.storage.get_resource_ids()
        self._validate_resource_id(resource_ids, resource_id)

        is_admin = self._check_whether_user_is_an_admin_or_not(user_id)

        if is_admin:
                self.storage.update_resource(
                    resource_id=resource_id,
                    resource_dto=resource_dto,
                    user_id=user_id
                )

        else:
            self.presenter.raise_user_cannot_manipulate_exception()


    def _check_whether_user_is_an_admin_or_not(self, user_id: int):
        service_adapter_obj = service_adapter.get_service_adapter()
        user_dtos = service_adapter_obj.auth_service.get_user_dtos([user_id])
        is_admin = user_dtos[0].is_admin
        return is_admin

    def _validate_resource_id(self, resource_ids: List[int], resource_id: int):
        if not resource_id in resource_ids:
            self.presenter.raise_invalid_id_exception()
