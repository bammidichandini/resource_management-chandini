from resource_management.interactors.storages.requests_storage_interface \
    import StorageInterface
from resource_management.interactors.presenters.presenter_interface \
    import PresenterInterface


class GetIndividualUserDetailsToAdmin:

    def __init__(
        self,
        storage: StorageInterface,
        presenter: PresenterInterface
    ):

        self.storage = storage
        self.presenter = presenter


    def get_individual_user_details_to_admin_interactor(
        self,
        user_id: int
    ):
        user_requests_dto = self.storage.get_individual_user_details_to_admin(
            user_id=user_id
            )

        response = self.presenter.get_individual_user_details_to_admin_response(
            user_requests_dto=user_requests_dto
            )

        return response
