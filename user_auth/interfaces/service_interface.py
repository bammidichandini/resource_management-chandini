from typing import List
from user_auth.interactors.get_users import GetAllUserDetailsInteractor
from user_auth.interactors.get_user_details_dtos import \
    GetUserDetailsInteractor
from user_auth.storages.authentication_storage import StorageImplementation


class ServiceInterface:

    @staticmethod
    def get_user_dtos(user_ids: List[int]):
        storage = StorageImplementation()
        interactor = GetUserDetailsInteractor(storage=storage)
        user_dtos = interactor.get_user_details_interactor(
            user_ids=user_ids
        )
        return user_dtos


    @staticmethod
    def get_all_user_dtos():
        storage = StorageImplementation()
        interactor = GetAllUserDetailsInteractor(storage=storage)
        user_dtos = interactor.get_user_details_interactor()
        return user_dtos
