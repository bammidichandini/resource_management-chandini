from typing import List
from user_auth.exceptions.exceptions import InvalidIdException
from user_auth.interactors.storages.storage_interface import StorageInterface
from user_auth.interactors.presenters.presenter_interface import PresenterInterface


class GetUserDetailsInteractor:
    def __init__(self, storage: StorageInterface):
        self.storage=storage

    def get_user_details_wrapper(
        self,
        user_ids: List[int],
        presenter: PresenterInterface
    ):

        try:
          return  self.get_user_details_interactor(user_ids)

        except InvalidIdException as error:
            presenter.raise_invalid_id_exception(error=error)

    def get_user_details_interactor(self, user_ids: List[int]):

        user_ids_list = self.storage.get_user_ids()
        self._validate_user_ids(user_ids_list, user_ids)

        response = self.storage.get_user_details_dto(user_ids)
        return response


    def _validate_user_ids(
        self,
        user_ids_list: List[int],
        user_ids: List[int]
    ):
        invalid_ids = []

        for user_id in user_ids:
            if not user_id in list(user_ids_list):
                invalid_ids.append(user_id)

        if invalid_ids:
            raise InvalidIdException(invalid_ids)
