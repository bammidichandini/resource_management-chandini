from resource_management.dtos.dtos import ResourceDto
from resource_management.exceptions.exceptions import InvalidIdException
from resource_management.interactors.storages.storage_interface import StorageInterface
from resource_management.interactors.presenters.presenter_interface import PresenterInterface


class GetResourceDetailsInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage


    def  get_resource_wrapper(
        self, resource_id: int, presenter: PresenterInterface
    ):
        try:
            return self.get_resource_response(resource_id=resource_id)
        except InvalidIdException:
            presenter.raise_invalid_id_exception()

    def get_resource_response(self, resource_id: int):

        self.storage.validate_resource_id(resource_id)

        resource_dto = self.storage.get_resource_details()

        return resource_dto
