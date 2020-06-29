from resource_management_v2.exceptions.exceptions \
    import InvalidOffsetOrLimit
from resource_management_v2.interactors.storages.multiple_storage_interface \
    import StorageInterface
from resource_management_v2.interactors.presenters.multiple_presenter_interface \
    import PresenterInterface
from resource_management_v2.interactors.get_resource_items \
    import GetResourceItemsInteractor
from resource_management_v2.interactors.get_resource \
    import GetResourceDetailsInteractor


class ResourceDetailsWithItemsInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def resource_details_with_items_interactor(
        self, presenter: PresenterInterface,
        resource_id: int, offset: int, limit: int
    ):
        try:
            return self.get_resource_details_with_items_response(
                offset=offset,
                limit=limit,
                resource_id=resource_id,
                presenter=presenter
            )
        except InvalidOffsetOrLimit:
            presenter.raise_invalid_offset_or_limit()

    def get_resource_details_with_items_response(
        self, offset: int, limit: int,
        resource_id: int, presenter: PresenterInterface
    ):
        resource_wrapper = GetResourceDetailsInteractor(
            storage=self.storage
        )

        resource_items_wrapper = GetResourceItemsInteractor(
            storage=self.storage
        )

        item_dtos = resource_items_wrapper.get_items_wrapper(
            resource_id=resource_id,
            presenter=presenter
        )

        resource_dto = resource_wrapper.get_resource_wrapper(
            resource_id=resource_id,
            presenter=presenter
        )
