from typing import List
from food_management.dtos.dtos import MealItemDto
from food_management.exceptions.exceptions import (
    InvalidMealId,
    InvalidItemId,
    InvalidQuantity,
    DuplicateItemsException
    )
from food_management.interactors.storages.storage_interface import StorageInterface
from food_management.interactors.presenters.presenter_interface import PresenterInterface


class CreateUserPreference:

    def __init__(self, storage: StorageInterface,
                 presenter: PresenterInterface
                 ):
        self.storage = storage
        self.presenter = presenter


    def create_user_preference_wrapper(
        self,
        meal_id: int,
        user_id: int,
        items_list_dto: List[MealItemDto]
    ):

        try:
            self.create_user_preference_interactor(
                meal_id=meal_id,
                user_id=user_id,
                items_list_dto=items_list_dto
            )
        except InvalidMealId:
            self.presenter.raise_invalid_meal_id()
        except InvalidItemId:
            self.presenter.raise_invalid_item_id()
        except InvalidQuantity:
            self.presenter.raise_invalid_quantity()

    def create_user_preference_interactor(
        self,
        meal_id: int,
        user_id: int,
        items_list_dto: List[MealItemDto]
    ):

        #TODO: validate_meal_id
        self.storage.validate_meal_id(meal_id=meal_id)

        #TODO: validate_item_id
        item_ids = self.storage.get_items_ids()
        invalid_items_list = self._validate_item_ids(items_list_dto, item_ids)
        empty_list = len(invalid_items_list) == 0
        non_empty_list not empty_list
        if non_empty_list:
            raise InvalidItemId(invalid_items_list)
        

        #TODO: validate_quantity
        invalid_quantity_items = self.storage._validate_quantity(items_list_dto)
        empty_list = len(invalid_items_list) == 0
        non_empty_list not empty_list
        if non_empty_list:
            raise InvalidQuanId(invalid_items_list)
        
        #TODO: check_for_duplicate_items

        #TODO: check_for_user_with_meal_id
        existed_meal = self.storage.check_for_user_with_meal_id(
            user_id=user_id,
            meal_id=meal_id
            )

        if existed_meal:
            pass
 
    
    @staticmethod
    def _validate_item_ids(items_list_dto, item_ids):
        invalid_items_list = []
        for item_dto in items_list_dto:
            if item_dto.item_id not in item_ids:
                invalid_items_list.append(item_dto.item_id)
        return invalid_items_list
        
    
    @staticmethod
    def _validate_quantity(items_list_dto):
        invalid_quantity_items = []
        for item_dto in items_list_dto:
            if item_dto.quantity <= 0:
                invalid_quantity_items.append(item_dto.item_id)
        return invalid_quantity_items