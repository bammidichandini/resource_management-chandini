from resource_management.dtos.dtos import ResourceItemParametersDto
from resource_management.interactors.storages.item_storages \
    import StorageInterface
from resource_management.adapters import service_adapter
from resource_management.interactors.presenters.presenter_interface \
    import PresenterInterface


class GetResourceItemsInteractor:

    def __init__(
        self,
        storage: StorageInterface,
        presenter: PresenterInterface
    ):

        self.storage = storage
        self.presenter = presenter


    def get_resource_items_interactor(
        self,
        user_id: int,
        req_parameter_dto: ResourceItemParametersDto
    ):

        valid_offset = self._check_for_valid_offset(
            req_parameter_dto.offset
        )

        invalid_offset = not valid_offset

        valid_input = self._check_for_valid_limit(req_parameter_dto.limit)

        invalid_input = not valid_input

        if invalid_input or invalid_offset:
            self.presenter.raise_invalid_input_exception()

        is_admin = self._check_whether_user_is_an_admin_or_not(user_id)

        if is_admin:
            items_dto_list = self.storage.get_resource_items(req_parameter_dto)

        else:
            self.presenter.raise_user_cannot_manipulate_exception()

        response = self.presenter.get_resource_items_response(
            items_dto = items_dto_list
            )

        return response


    def _check_whether_user_is_an_admin_or_not(self, user_id: int):
        service_adapter_obj = service_adapter.get_service_adapter()
        user_dtos = service_adapter_obj.auth_service.get_user_dtos([user_id])
        is_admin = user_dtos[0].is_admin
        return is_admin


    def _check_for_valid_limit(self, limit) -> bool:
        if limit <= 0 :
            return False
        return True

    def _check_for_valid_offset(self, offset):
        if offset < 0:
            return False
        return True
