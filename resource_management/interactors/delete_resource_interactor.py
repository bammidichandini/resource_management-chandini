from typing import List
from django.core.exceptions import ObjectDoesNotExist
from resource_management.adapters import service_adapter
from resource_management.interactors.storages.resources_storage_interface \
    import StorageInterface
from resource_management.interactors.presenters.presenter_interface \
    import PresenterInterface


class DeleteResourcesInteractor:

    def __init__(
        self,
        storage: StorageInterface,
        presenter: PresenterInterface
    ):
        self.storage = storage
        self.presenter = presenter


    def  delete_resources_interactor(
        self,
        user_id: int,
        resource_ids_list: List[int]
    ):

        resource_ids = self.storage.get_resource_ids()
        self._validate_resource_ids(resource_ids, resource_ids_list)
        is_admin = self._check_whether_user_is_an_admin_or_not(user_id)


        if is_admin:
                self.storage.delete_resources(
                    user_id=user_id,
                    resource_ids_list=resource_ids_list
                    )

        else:
            self.presenter.raise_user_cannot_manipulate_exception()

    def _check_whether_user_is_an_admin_or_not(self, user_id: int):
        service_adapter_obj = service_adapter.get_service_adapter()
        user_dtos = service_adapter_obj.auth_service.get_user_dtos([user_id])
        is_admin = user_dtos[0].is_admin
        return is_admin

    def _validate_resource_ids(self, resource_ids: List[int], resource_ids_list: List[int]):
        invalid_ids = []
        for resource_id in resource_ids_list:
            if not resource_id in resource_ids:
                invalid_ids.append(resource_id)

        if invalid_ids:
            self.presenter.raise_invalid_id_exception()
