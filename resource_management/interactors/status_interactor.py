from typing import List
from resource_management.interactors.storages.requests_storage_interface \
    import StorageInterface
from resource_management.interactors.presenters.presenter_interface \
    import PresenterInterface


class StatusInteractor:

    def __init__(
        self,
        storage: StorageInterface,
        presenter: PresenterInterface
    ):

        self.storage = storage
        self.presenter = presenter


    def status_interactor(
        self, status: str,
        reason: str,
        request_ids_list: List[int]
    ):

        request_ids = self.storage.get_request_ids()

        self._validate_request_ids(request_ids, request_ids_list)

        self.storage.set_status(
            status=status,
            reason=reason,
            request_ids_list=request_ids_list
        )

    def _validate_request_ids(
        self, request_ids: List[int], request_ids_list: List[int]):
            invalid_ids = []
            for id in request_ids:
                if id not in request_ids_list:
                    invalid_ids.append(id)

            if invalid_ids:
                self.presenter.raise_invalid_id_exception()
