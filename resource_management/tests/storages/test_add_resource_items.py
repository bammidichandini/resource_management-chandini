import pytest
from resource_management.models import Item
from resource_management.storages.item_storages_implementation import StorageImplementation


@pytest.mark.django_db
def test_add_resource_items_storage(create_items,
                                    reitems_dto,
                                   ):

    #arrange

    user_id = 1
    reitem_dtos = reitems_dto

    storage = StorageImplementation()

    #act
    storage.create_item(
        item_dto=reitem_dtos,
        user_id=user_id
        )

    #assert
    Item.objects.filter(
        name=reitem_dtos.item_name,
        link=reitem_dtos.link,
        description=reitem_dtos.description
        ).exists()
