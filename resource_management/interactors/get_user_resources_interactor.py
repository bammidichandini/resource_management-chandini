from resource_management.interactors.storages.resources_storage_interface \
    import StorageInterface
from resource_management.interactors.presenters.presenter_interface \
    import PresenterInterface


class GetUserResourcesInteractor:

    def __init__(
        self,
        storage: StorageInterface,
        presenter: PresenterInterface
    ):
        self.storage = storage
        self.presenter = presenter

    def get_user_resources_interactor(self, user_id: int):

        items_dto = self.storage.get_user_resources(user_id=user_id)

        response = self.presenter.get_user_resources_response(
            items_dto=items_dto
            )

        return response
