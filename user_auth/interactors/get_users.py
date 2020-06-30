from typing import List
from user_auth.exceptions.exceptions import InvalidIdException
from user_auth.interactors.storages.storage_interface import StorageInterface
from user_auth.interactors.presenters.presenter_interface import PresenterInterface


class GetAllUserDetailsInteractor:
    def __init__(
        self, storage: StorageInterface, presenter: PresenterInterface):
        self.storage=storage
        self.presenter=presenter

    # def get_user_details_wrapper(self):
    #     response = self.get_user_details_interactor()


    def get_user_details_interactor(self):

        user_ids = self.storage.get_user_ids()

        response = self.storage.get_user_details_dto(user_ids)
        return response
