import pytest
from resource_management.storages.item_storages_implementation import StorageImplementation


@pytest.mark.django_db
def test_get_request_storage(create_requests,
                              get_requests
                              ):
    # arrange

    expected_response = get_requests
    storage = StorageImplementation()

    # act

    actual_response = storage.get_requests()

    # assert

    assert expected_response[0].name == actual_response[0].name
    assert expected_response[0].resource_name == actual_response[0].resource_name
    assert expected_response[0].item_name == actual_response[0].item_name
    assert expected_response[0].access_level == actual_response[0].access_level
