from resource_management.interactors.storages.resources_storage_interface import StorageInterface
from resource_management.interactors.presenters.presenter_interface import PresenterInterface
from resource_management.exceptions.exceptions import (
    UserCannotManipulateException,
    InvalidDetailsException,
    InvalidIdException
    )
from resource_management.dtos.dtos import ResourceDto
from django.core.exceptions import ObjectDoesNotExist


class UpdateResourceInteractor:

    def __init__(self, storage: StorageInterface,
                 presenter: PresenterInterface
                 ):
        self.storage = storage
        self.presenter = presenter

    def update_resource_interactor(self,
                                  resource_id: int,
                                  resource_dto: ResourceDto,
                                  user_id: int
                                  ):

        ids_list = [resource_id]
        valid_input = self.storage.check_for_valid_input(ids_list)

        invalid_input = not valid_input
        if invalid_input:
            self.presenter.raise_invalid_id_exception()
        is_admin = self.storage.is_admin(user_id)

        if is_admin:
            try:
                self.storage.update_resource(
                    resource_id=resource_id,
                    resource_dto=resource_dto,
                    user_id=user_id
                    )
            except ObjectDoesNotExist:
                self.presenter.raise_invalid_id_exception()
        else:
            self.presenter.raise_user_cannot_manipulate_exception()
