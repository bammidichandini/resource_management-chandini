from resource_management.interactors.storages.item_storages \
    import StorageInterface
from resource_management.interactors.presenters.presenter_interface \
    import PresenterInterface
from resource_management.adapters import service_adapter
from resource_management.dtos.dtos import RequestsDto


class GetRequestsInteractor:

    def __init__(
        self,
        storage: StorageInterface,
        presenter: PresenterInterface
    ):

        self.storage = storage
        self.presenter = presenter


    def get_requests_interactor(
        self,
        user_id: int
    ):

        service_adapter_obj = service_adapter.get_service_adapter()
        user_dtos = service_adapter_obj.auth_service.get_user_dtos([user_id])

        request_dtos =  self.storage.get_requests()

        response = self.presenter.get_requests_response(
            user_dtos=user_dtos,
            request_dto=request_dtos
            )

        return response
