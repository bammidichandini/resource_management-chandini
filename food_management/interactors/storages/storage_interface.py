from abc import ABC
from abc import abstractmethod
from typing import List
from datetime import datetime
from food_management.dtos.dtos import MealItemDto


class StorageInterface(ABC):

    @abstractmethod
    def validate_meal_id(self, meal_id: int):
        pass

    @abstractmethod
    def validate_item_id(self, items_list_dto: List[MealItemDto]):
        pass

    @abstractmethod
    def validate_quantity(self, items_list_dto: List[MealItemDto]):
        pass

    @abstractmethod
    def check_for_duplicate_items(self, items_list_dto: List[MealItemDto]):
        pass

    @abstractmethod
    def check_for_user_with_meal_id(self, user_id: int, meal_id: int) -> bool:
        pass

    @abstractmethod
    def get_meal_items_ids(self, meal_id: int) -> List[int]:
        pass

    @abstractmethod
    def update_the_meal(
        self,
        user_id: int,
        meal_id: int,
        items_list_dto: List[MealItemDto]
    ):
        pass

    @abstractmethod
    def create_the_meal(
        self,
        user_id: int,
        meal_id: int,
        items_list_dto: List[MealItemDto]
    ):
        pass

    @abstractmethod
    def get_datetime_object_to_meal(self, meal_id) -> datetime:
        pass


    # @abstractmethod
    # def get_items_ids(self):
    #     pass
