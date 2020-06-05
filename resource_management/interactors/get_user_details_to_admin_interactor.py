from resource_management.interactors.storages.user_details_to_admin_storages import StorageInterface
from resource_management.interactors.presenters.presenter_interface import PresenterInterface


class GetUserDetailsToAdminInteractor:

    def __init__(self, storage: StorageInterface,
                 presenter: PresenterInterface
                 ):
        self.storage = storage
        self.presenter = presenter

    def get_user_details_to_admin_interactor(self):
        user_dto = self.storage.get_user_details_to_admin()

        response = self.presenter.get_user_details_to_admin_response(
            user_dto=user_dto
            )
        return response