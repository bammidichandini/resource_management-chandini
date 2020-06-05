from resource_management.interactors.storages.resources_storage_interface import StorageInterface
from resource_management.interactors.presenters.presenter_interface import PresenterInterface
from resource_management.exceptions.exceptions import UserCannotManipulateException


class UpdateResourceInt:

    def __init__(self, storage: StorageInterface,
                 presenter: PresenterInterface
                 ):
        self.storage = storage
        self.presenter = presenter

    def update_resource_interface(self,
                                  resource_id: int,
                                  is_admin: str,
                                  image_url: str,
                                  name: str,
                                  item_name: str,
                                  link: str,
                                  description: str
                                  ):
        try:
            self.storage.update_resource(
                resource_id=resource_id,
                is_admin=is_admin,
                image_url=image_url,
                name=name,
                item_name=item_name,
                link=link,
                description=description
                )
        except UserCannotManipulateException:
            self.presenter.raise_user_cannot_manipulate_exception()


