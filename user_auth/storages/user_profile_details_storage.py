from user_auth.interactors.storages.user_profile_storage_interface \
        import StorageInterface
from abc import ABC
from abc import abstractmethod
from user_auth.models import User
from user_auth.dtos.dtos import UpdateProfileDto
from django.contrib.auth import *


class StorageImplementation(StorageInterface):


    def update_user_details(self,
                            user_id: int,
                            user_profile_dto: UpdateProfileDto
                            ):

        User.objects.filter(id=user_id).update(
            name=user_profile_dto.name,
            email=user_profile_dto.email,
            gender=user_profile_dto.gender,
            job_role=user_profile_dto.job_role,
            department=user_profile_dto.department
            )


    def update_password(self, user_id: int, password: str):
        user = User.objects.get(id=user_id)
        user.set_password(password)
        user.save()
