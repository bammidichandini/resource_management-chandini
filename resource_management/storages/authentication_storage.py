from resource_management.models import User
from common.dtos import UserAuthTokensDTO
from resource_management.exceptions.exceptions import (
    InvalidUserException,
    InvalidPasswordException,
    UserAlreadyExistedException
    )
from resource_management.interactors.storages.storage_interface import \
    StorageInterface

from django.contrib.auth.hashers import make_password


class StorageImplementation(StorageInterface):

    def validate_username(self, username: str):
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            raise InvalidUserException

    def check_for_valid_offset(self, offset):
        if offset < 0:
            return False
        return True

    def validate_password(self,
                          username: str,
                          password: str) \
                           -> int:
        try:
            user_obj = User.objects.get(
                username=username
                )

        except User.DoesNotExist:
            raise InvalidUserException
            return

        if not user_obj.check_password(password):
            raise InvalidPasswordException


        return user_obj.id

    def is_user_exists(self,username: str):
        user = User.objects.filter(username=username).exists()
        return user

    def create_a_new_user(self,
                          username: str,
                          password: str
                          ) -> int:

        user = User.objects.create(username=username,
                            password=make_password(password)
                            )

        return user.id

    def is_admin(self, user_id: int) -> bool:
        is_admin = User.objects.get(id=user_id).is_admin
        return is_admin
