import pytest
from resource_management.storages.resources_storage \
    import StorageImplementation


@pytest.mark.django_db
def test_get_user_resources(
    items_dto,
    create_users1,
    create_useraccess,
    create_items,
    create_resources,
    create_requests
):

    # arrange
    user_id = 1
    expected_dto = items_dto

    storage = StorageImplementation()

    # act
    actual_dto = storage.get_user_resources(
        user_id=user_id
        )

    # assert
    assert actual_dto[0].resource_name == expected_dto[0].resource_name
    assert actual_dto[0].item_name == expected_dto[0].item_name
    assert actual_dto[0].link == expected_dto[0].link

