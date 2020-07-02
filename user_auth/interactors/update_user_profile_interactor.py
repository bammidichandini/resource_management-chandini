from user_auth.dtos.dtos import UpdateProfileDto
from user_auth.interactors.storages.user_profile_storage_interface import StorageInterface
from user_auth.interactors.presenters.presenter_interface import PresenterInterface


class UpdateUserProfileInteractor:

    def __init__(
        self,
        storage: StorageInterface,
        presenter: PresenterInterface
    ):

        self.storage = storage
        self.presenter = presenter


    def update_user_details_interactor(
        self,
        user_id: int,
        user_profile_dto: UpdateProfileDto
    ):

        self.storage.update_user_details(
                user_id=user_id,
                user_profile_dto=user_profile_dto
        )
