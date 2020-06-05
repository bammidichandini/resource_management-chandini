from resource_management.interactors.storages.resources_storage_interface import StorageInterface
from resource_management.interactors.presenters.presenter_interface import PresenterInterface
from resource_management.exceptions.exceptions import UserCannotManipulateException
from resource_management.dtos.dtos import ResourceDto


class CreateResourceInteractor:

    def __init__(self, storage: StorageInterface,
                 presenter: PresenterInterface
                 ):
        self.storage = storage
        self.presenter = presenter


    def create_resource_interactor(self,
                                   resource_dto: ResourceDto,
                                   user_id
                                  ):

        is_admin = self.storage.is_admin(user_id)

        if is_admin:
            self.storage.create_resource(resource_dto=resource_dto, user_id=user_id)
        else:
            self.presenter.raise_user_cannot_manipulate_exception()
