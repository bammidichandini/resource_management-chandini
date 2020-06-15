from resource_management.interactors.storages.requests_storage_interface \
    import StorageInterface
from resource_management.interactors.presenters.presenter_interface \
    import PresenterInterface
from resource_management.exceptions.exceptions import InvalidIdException


class DeleteUserRequestInteractor:

    def __init__(
        self,
        storage: StorageInterface,
        presenter: PresenterInterface
    ):

        self.storage = storage
        self.presenter = presenter

    def delete_user_request_wrapper(self, user_id: int, request_id: int):

        try:
          self.delete_user_request_interactor(user_id=user_id, request_id=request_id)
        except InvalidIdException:
          self.presenter.raise_invalid_id_exception()
        return


    def delete_user_request_interactor(
        self,
        user_id: int,
        request_id: int
    ):

        ids_list = [request_id]
        valid_input = self.storage.check_for_valid_input(ids_list)

        invalid_input = not valid_input

        if invalid_input:
            raise InvalidIdException

        self.storage.delete_user_request(
            user_id=user_id,
            request_id=request_id
        )
