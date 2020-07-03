from user_auth.models import User
from user_auth.storages.authentication_storage import StorageImplementation
from user_auth.interactors.storages.storage_interface import StorageInterface
from user_auth.exceptions.exceptions import InvalidPasswordException
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
