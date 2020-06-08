from resource_management.dtos.dtos import ItemDto
from resource_management.interactors.storages.item_storages \
    import StorageInterface
from resource_management.interactors.presenters.presenter_interface \
    import PresenterInterface


class CreateResourceItemInteractor:

    def __init__(
        self,
        storage: StorageInterface,
        presenter: PresenterInterface
    ):
        self.storage = storage
        self.presenter = presenter


    def create_item_interactor(
        self,
        item_dto: ItemDto,
        user_id: int
    ):
        is_admin = self.storage.is_admin(user_id)
        if is_admin:
            self.storage.create_item(
                item_dto=item_dto,
                user_id=user_id
            )
        else:
            self.presenter.raise_user_cannot_manipulate_exception()
