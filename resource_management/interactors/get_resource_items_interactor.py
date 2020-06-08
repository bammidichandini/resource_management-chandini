from resource_management.dtos.dtos import ResourceItemParametersDto
from resource_management.interactors.storages.item_storages \
    import StorageInterface
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

        ids_list = [req_parameter_dto.limit]

        valid_offset = self.storage.check_for_valid_offset(
            req_parameter_dto.offset
        )

        invalid_offset = not valid_offset

        valid_input = self.storage.check_for_valid_input(ids_list)

        invalid_input = not valid_input

        if invalid_input or invalid_offset:
            self.presenter.raise_invalid_id_exception()

        is_admin = self.storage.is_admin(user_id=user_id)

        if is_admin:
            items_dto_list = self.storage.get_resource_items(req_parameter_dto)

        else:
            self.presenter.raise_user_cannot_manipulate_exception()

        response = self.presenter.get_resource_items_response(
            items_dto = items_dto_list
            )

        return response
