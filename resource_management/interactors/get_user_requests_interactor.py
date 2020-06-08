from resource_management.exceptions.exceptions \
    import InvalidDetailsException
from resource_management.interactors.storages.requests_storage_interface \
    import StorageInterface
from resource_management.interactors.presenters.presenter_interface \
    import PresenterInterface


class GetUserRequestsInteractor:

    def __init__(
        self,
        storage: StorageInterface,
        presenter: PresenterInterface
    ):

        self.storage = storage
        self.presenter = presenter


    def get_user_requests_interactor(
        self,
        user_id: int,
        offset: int,
        limit: int
    ):

        list_ids = [limit]

        valid_input = self.storage.check_for_valid_input(list_ids)
        invalid_input = not valid_input

        valid_offset = self.storage.check_for_valid_offset(offset)
        invalid_offset = not valid_offset

        if invalid_offset or invalid_input:
            self.presenter.raise_invalid_id_exception()

        user_dto = self.storage.get_user_requests(
            user_id=user_id,
            offset=offset,
            limit=limit
        )

        response = self.presenter.get_user_requests_response(user_dto=user_dto)

        return response
