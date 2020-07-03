import pytest
from user_auth.models import User
from user_auth.storages.authentication_storage import StorageImplementation


@pytest.mark.django_db
def test_user_signup(create_users1):

    # arrrange

    username = "Suresh"
    password = "Password"

    storage = StorageImplementation()

    # act
    storage.create_a_new_user(
        username=username,
        password=password
        )

    # assert
    User.objects.filter(username=username).exists()
    User.objects.get(username=username)


@pytest.mark.django_db
def test_user_signup_with_existed_user_raises_exception(create_users1):

    # arrrange

    username = "suman"
    password = "suman"

    storage = StorageImplementation()

    # act
    storage.create_a_new_user(
        username=username,
        password=password
        )

    # assert
    User.objects.filter(username=username).exists()
    User.objects.get(username=username)

@pytest.mark.django_db
def test_is_user_exists(create_users1):

    # arrange
    username = "chandini"
    expected_value = True

    storage = StorageImplementation()

    # act
    actual_value = storage.is_user_exists(username)

    # assert
    assert actual_value == expected_value