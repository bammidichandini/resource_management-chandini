from resource_management.models import User
from resource_management.storages.authentication_storage import StorageImplementation
from resource_management.interactors.storages.storage_interface import StorageInterface
from resource_management.exceptions.exceptions import InvalidPasswordException
import pytest

@pytest.mark.django_db()
def test_validate_password(create_users1):

    #arrange
    username = "madhuri"
    password = "super"
    storage = StorageImplementation()

    #act
    with pytest.raises(InvalidPasswordException):
        storage.validate_password(
            username=username,
            password=password
        )
