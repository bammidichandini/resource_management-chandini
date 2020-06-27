from typing import List
from resource_management.exceptions.exceptions import InvalidIdException
from django.core.exceptions import ObjectDoesNotExist
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

        is_admin = self.storage.is_admin(user_id)

        if is_admin:
            try:
                self.storage.delete_resources(
                    user_id=user_id,
                    resource_ids_list=resource_ids_list
                    )
            except InvalidIdException:
                self.presenter.raise_invalid_id_exception()

        else:
            self.presenter.raise_user_cannot_manipulate_exception()
