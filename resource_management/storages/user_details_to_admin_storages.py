from abc import ABC
from abc import abstractmethod
from typing import List
from common.dtos import UserAuthTokensDTO
from resource_management.dtos.dtos import RegisterUserDto
from resource_management.models import User
from resource_management.interactors.storages.user_details_to_admin_storages \
  import StorageInterface


class StorageImplementation(StorageInterface):

  def get_user_details_to_admin(self) -> List[RegisterUserDto]:

      users = list(User.objects.filter(is_admin=False))
      list_of_user_dtos = []
      for user in users:
        list_of_user_dtos.append(RegisterUserDto(
                                    person_name=user.name,
                                    department=user.department,
                                    job_role=user.job_role,
                                    url=user.profile_pic
                                    )
                                    )
      return list_of_user_dtos
