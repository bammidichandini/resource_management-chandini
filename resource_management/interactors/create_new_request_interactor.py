from resource_management.interactors.storages.requests_storage_interface \
    import StorageInterface
from resource_management.interactors.presenters.presenter_interface \
    import PresenterInterface
from resource_management.dtos.dtos import CreateUserRequestsDto


class CreateNewRequestInteractor:

    def __init__(
        self,
        storage: StorageInterface,
        presenter: PresenterInterface
    ):
        self.storage = storage
        self.presenter = presenter

    def create_new_request_interactor(
        self,
        user_id: int,
        request_dto: CreateUserRequestsDto
    ):
        self.storage.create_new_user_request(
            user_id=user_id,
            request_dto=request_dto
        )