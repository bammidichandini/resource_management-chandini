from resource_management.interactors.storages.user_profile_storage_interface \
        import StorageInterface
from abc import ABC
from abc import abstractmethod
from resource_management.models import User
from resource_management.dtos.dtos import UpdateProfileDto
from resource_management.exceptions.exceptions import InvalidDetailsException
from django.contrib.auth import *


class StorageImplementation(StorageInterface):


    def update_user_details(self,
                            user_id: int,
                            user_profile_dto: UpdateProfileDto
                            ):
        invalid_details = (not(type(user_profile_dto.name) == str)
                            or not(type(user_profile_dto.email) == str)
                            or not(type(user_profile_dto.gender) == str)
                            or not(type(user_profile_dto.job_role) == str)
                            or not(type(user_profile_dto.department) == str))
        if invalid_details:
            raise InvalidDetailsException

        User.objects.filter(id=user_id).update(
            name=user_profile_dto.name,
            email=user_profile_dto.email,
            gender=user_profile_dto.gender,
            job_role=user_profile_dto.job_role,
            department=user_profile_dto.department
            )


    def update_password(self, user_id: int, password: str):
        user = User.objects.get(id=user_id)
        user.set_password(user.password)
        user.save()