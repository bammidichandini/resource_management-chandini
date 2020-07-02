from resource_management.models.user import User
from resource_management.storages.authentication_storage import StorageImplementation
from resource_management.exceptions.exceptions import InvalidUserException
import pytest

@pytest.mark.django_db()
def test_validate_username(create_users1):

    #arrange
    username = "super"
    storage = StorageImplementation()

    #act
    with pytest.raises(InvalidUserException):
        storage.validate_username(username=username)


@pytest.mark.django_db()
def test_validate_username_with_valid_username(create_users1):

    #arrange
    username = "madhuri"
    storage = StorageImplementation()

    #act
    storage.validate_username(username=username)
