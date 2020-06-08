from resource_management.interactors.storages.resources_storage_interface \
    import StorageInterface
from resource_management.interactors.presenters.presenter_interface \
    import PresenterInterface


class GetResourcesInteractor:

    def __init__(
        self,
        storage: StorageInterface,
        presenter: PresenterInterface
    ):

        self.storage = storage
        self.presenter = presenter


    def get_resources_interactor(self):

        resources_dto_list = self.storage.get_resources()

        response = self.presenter.get_resources_response(
            resources_dto_list = resources_dto_list
            )

        return response
