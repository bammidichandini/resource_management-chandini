from resource_management.interactors.storages.requests_storage_interface import StorageInterface
from resource_management.interactors.presenters.presenter_interface import PresenterInterface
from resource_management.exceptions.exceptions import InvalidDetailsException


class GetUserRequestsInteractor:

    def __init__(self,storage: StorageInterface,
                 presenter: PresenterInterface
    ):
        self.storage = storage
        self.presenter = presenter

    def get_user_requests_interactor(self, user_id: int):

        try:
            user_dto = self.storage.get_user_requests(user_id=user_id)

        except InvalidDetailsException:
            self.presenter.raise_invalid_details_exception()

        response = self.presenter.get_user_requests_response(user_dto)

        return response
