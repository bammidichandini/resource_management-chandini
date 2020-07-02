from typing import List
from resource_management.interactors.storages.requests_storage_interface \
    import StorageInterface
from resource_management.interactors.presenters.presenter_interface \
    import PresenterInterface
from resource_management.dtos.dtos import RequestsUpdateDto


class UpdateUserRequestInteractor:

    def __init__(
        self,
        storage: StorageInterface,
        presenter: PresenterInterface
    ):

        self.storage = storage
        self.presenter = presenter


    def update_user_request_interactor(
        self,
        user_id: int,
        request_id: int,
        update_dto: RequestsUpdateDto
    ):
        # ids_list = [request_id]

        # valid_input = self.storage.check_for_valid_input(ids_list)

        # invalid_input = not valid_input

        # if invalid_input:
        #     self.presenter.raise_invalid_id_exception()

        request_ids = self.storage.get_request_ids()
        self._validate_request_id(request_ids, request_id)

        self.storage.update_user_request(
                    user_id=user_id,
                    request_id=request_id,
                    update_dto=update_dto
        )

    def _validate_request_id(self, request_ids: List[int], request_id: int):
        if request_id not in request_ids:
            self.presenter.raise_invalid_id_exception()
