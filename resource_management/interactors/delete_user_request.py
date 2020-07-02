from typing import List
from resource_management.exceptions.exceptions import InvalidIdException
from resource_management.interactors.storages.requests_storage_interface \
    import StorageInterface
from resource_management.interactors.presenters.presenter_interface \
    import PresenterInterface


class DeleteUserRequestInteractor:

    def __init__(
        self,
        storage: StorageInterface,
        presenter: PresenterInterface
    ):

        self.storage = storage
        self.presenter = presenter


    def delete_user_request_interactor(
        self,
        user_id: int,
        request_id: int
    ):
        request_ids = self.storage.get_request_ids()
        self._validate_request_id(request_ids, request_id)
        self.storage.delete_user_request(
            user_id=user_id,
            request_id=request_id
        )

    def _validate_request_id(self, request_ids: List[int], request_id: int):
        if request_id not in request_ids:
            self.presenter.raise_invalid_id_exception()

