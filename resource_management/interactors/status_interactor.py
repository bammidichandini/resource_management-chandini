from typing import List
from resource_management.exceptions.exceptions import (
    InvalidDetailsException,
    InvalidIdException
    )
from resource_management.interactors.storages.requests_storage_interface \
    import StorageInterface
from resource_management.interactors.presenters.presenter_interface \
    import PresenterInterface
from django.core.exceptions import ObjectDoesNotExist



class StatusInteractor:

    def __init__(self,
                 storage: StorageInterface,
                 presenter: PresenterInterface
                ):
        self.storage = storage
        self.presenter = presenter

    def status_interactor(self, status: str,
                          reason: str,
                          request_ids_list: List[int]
                          ):

        valid_input = self.storage.check_for_valid_input(request_ids_list)

        invalid_input = not valid_input
        if invalid_input:
            self.presenter.raise_invalid_id_exception()

        self.storage.set_status(status=status,
                                    reason=reason,
                                    request_ids_list=request_ids_list
                                    )
