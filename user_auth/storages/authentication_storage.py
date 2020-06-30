from typing import List
from common.dtos import UserAuthTokensDTO
from user_auth.models import User
from user_auth.dtos.dtos import userdto
from user_auth.exceptions.exceptions import (
    InvalidUserException,
    InvalidPasswordException
    )
from user_auth.interactors.storages.storage_interface import \
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

    def get_user_details_dtos(self, user_ids: List[int]) \
        -> List[userdto]:
            user_dtos = []
            users = User.objects.filter(id__in=user_ids)
            for user in list(users):
                user_dtos.append(userdto(
                    id=user.id,
                    person_name=user.name,
                    department=user.department,
                    job_role=user.job_role,
                    is_admin=user.is_admin
                ))
            return user_dtos

    def get_user_ids(self) -> List[int]:
        users = User.objects.all().values_list('id', flat=True)
        return users

    def get_all_user_details_to_admin(self):
        users = User.objects.filter(is_admin=False)
        user_dtos = []
        for user in list(users):
            user_dtos.append(
                userdto(
                    id=user.id,
                    person_name=user.name,
                    department=user.department,
                    job_role=user.job_role,
                    profile_pic=user.profile_pic,
                    is_admin=user.is_admin
                )
            )
