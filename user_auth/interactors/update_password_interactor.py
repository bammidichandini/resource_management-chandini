from user_auth.interactors.storages.user_profile_storage_interface \
    import StorageInterface
from user_auth.interactors.presenters.presenter_interface \
    import PresenterInterface


class UpdatePasswordInteractor:

    def __init__(
        self,
        storage: StorageInterface,
        presenter: PresenterInterface
    ):

        self.storage = storage
        self.presenter = presenter

    def update_password_interactor(
        self,
        password: str,
        user_id: int
    ):

        self.storage.update_password(
            user_id=user_id,
            password=password
        )
