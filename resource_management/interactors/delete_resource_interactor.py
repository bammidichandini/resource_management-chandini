from typing import List
from resource_management.exceptions.exceptions import (
    UserCannotManipulateException,
    InvalidIdException
    )
from resource_management.interactors.storages.resources_storage_interface import StorageInterface
from resource_management.interactors.presenters.presenter_interface import PresenterInterface


class DeleteResourcesInteractor:

    def __init__(self, storage: StorageInterface,
                 presenter: PresenterInterface
                 ):
        self.storage = storage
        self.presenter = presenter

    def  delete_resources_interactor(self,
                                    user_id: int,
                                    resource_ids_list: List[int]):

        valid_input = self.storage.check_for_valid_input(resource_ids_list)

        invalid_input = not valid_input
        if invalid_input:
            self.presenter.raise_invalid_id_exception()

        is_admin = self.storage.is_admin(user_id)
        if is_admin:
            self.storage.delete_resources(
                user_id=user_id,
                resource_ids_list=resource_ids_list
                )
        else:
            self.presenter.raise_user_cannot_manipulate_exception()
