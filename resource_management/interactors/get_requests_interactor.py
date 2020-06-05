from resource_management.interactors.storages.item_storages \
    import StorageInterface
from resource_management.interactors.presenters.presenter_interface \
    import PresenterInterface
from resource_management.dtos.dtos import RequestsDto


class GetRequestsInteractor:

    def __init__(self, storage: StorageInterface,
                 presenter: PresenterInterface
                 ):
        self.storage = storage
        self.presenter = presenter

    def get_requests_interactor(self, user_id: int):
        request_dto =  self.storage.get_requests()

        response = self.presenter.get_requests_response(
            request_dto
            )

        return response
