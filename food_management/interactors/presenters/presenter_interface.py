from abc import ABC
from abc import abstractmethod
from typing import List
from food_management.exceptions.exceptions import (
    InvalidItemId,
    InvalidQuantity,
    DuplicateItemsException,
    MissedItemsException
)


class PresenterInterface(ABC):

    @abstractmethod
    def raise_invalid_meal_id(self):
        pass

    @abstractmethod
    def raise_invalid_item_id(self, error: InvalidItemId):
        pass

    @abstractmethod
    def raise_invalid_quantity(self, error: InvalidQuantity):
        pass

    @abstractmethod
    def raise_duplicate_items(self, error: DuplicateItemsException):
        pass

    @abstractmethod
    def raise_missed_items(self, error: MissedItemsException):
        pass

    @abstractmethod
    def raise_invalid_time(self):
        pass
