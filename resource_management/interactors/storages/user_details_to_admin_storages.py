from abc import ABC
from abc import abstractmethod
from typing import List
from common.dtos import UserAuthTokensDTO
from resource_management.dtos.dtos import RegisterUserDto


class StorageInterface(ABC):

  @abstractmethod
  def get_user_details_to_admin(self) -> List[RegisterUserDto]:
      pass