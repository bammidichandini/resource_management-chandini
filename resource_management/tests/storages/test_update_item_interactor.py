import pytest
from resource_management.models import Item
from resource_management.exceptions.exceptions import UserCannotManipulateException
from resource_management.storages.item_storages_implementation import StorageImplementation


@pytest.mark.django_db
def test_update_resource_storage(create_items,
                                 reitems_dto,
                                 create_users1
                                 ):

    #arrange

    item_id = 1
    user_id = 1
    item_dto = reitems_dto

    storage = StorageImplementation()

    #act
    storage.update_item(
        item_dto=item_dto,
        user_id=user_id,
        item_id=item_id
        )

    #assert
    Item.objects.filter(
        name=item_dto.item_name,
        link=item_dto.link,
        description=item_dto.description
        ).exists()


