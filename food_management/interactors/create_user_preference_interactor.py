from typing import List
from food_management.dtos.dtos import MealItemDto
from datetime import datetime, timedelta
from food_management.exceptions.exceptions import (
    InvalidMealId,
    InvalidItemId,
    InvalidQuantity,
    DuplicateItemsException,
    MissedItemsException,
    InvalidTimeException,
    NoItemId
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
        except InvalidItemId as error:
            self.presenter.raise_invalid_item_id(error=error)
        except InvalidQuantity as error:
            self.presenter.raise_invalid_quantity(error=error)
        except DuplicateItemsException as error:
            self.presenter.raise_duplicate_items(error=error)
        except MissedItemsException as error:
            self.presenter.raise_missed_items(error=error)
        except InvalidTimeException:
            self.presenter.raise_invalid_time()


    def create_user_preference_interactor(
        self,
        meal_id: int,
        user_id: int,
        items_list_dto: List[MealItemDto]
    ):

        #TODO: validate_meal_id

        self.storage.validate_meal_id(meal_id=meal_id)


        # #TODO: validate items_ids

        # item_ids = self.storage.get_items_ids()
        # self._validate_item_ids(items_list_dto, item_ids)


        #TODO: validate_meal_item_id

        item_ids = self.storage.get_meal_items_ids(meal_id=meal_id)
        self._validate_item_ids(items_list_dto, item_ids)


        #TODO: validate_quantity
        self._validate_quantity(items_list_dto)


        #TODO: check_for_duplicate_items
        self._get_duplicate_items(items_list_dto, item_ids)


        #TODO: validate_datetime
        end_datetime = self.storage.get_datetime_object_to_meal(
            meal_id=meal_id
        )
        self._validate_datetime(end_datetime)


        #TODO: check_for_user_with_meal_id
        existed_meal = self.storage.check_for_user_with_meal_id(
            user_id=user_id,
            meal_id=meal_id
            )

        if existed_meal:
            self.storage.update_the_meal(
                meal_id=meal_id,
                user_id=user_id,
                items_list_dto=items_list_dto
            )

        else:
            self.storage.create_the_meal(
                meal_id=meal_id,
                user_id=user_id,
                items_list_dto=items_list_dto
            )

    @staticmethod
    def _validate_item_ids(items_list_dto, item_ids):
        invalid_items_list = []
        for item_dto in items_list_dto:
            if item_dto.item_id not in item_ids:
                invalid_items_list.append(item_dto.item_id)

        empty_list = len(invalid_items_list) == 0
        non_empty_list = not empty_list

        if non_empty_list:
            raise InvalidItemId(items_list=invalid_items_list)



    @staticmethod
    def _validate_quantity(items_list_dto):
        invalid_quantity_items = []
        for item_dto in items_list_dto:
            if item_dto.quantity < 0:
                invalid_quantity_items.append(item_dto.item_id)

        empty_list = len(invalid_quantity_items) == 0
        non_empty_list = not empty_list

        if non_empty_list:
            raise InvalidQuantity(invalid_quantity_items)



    @staticmethod
    def _get_duplicate_items(items_list_dto, item_ids):
        duplicate_items_list = []
        items_list = []
        for item_dto in items_list_dto:
            if item_dto.item_id not in items_list:
                items_list.append(item_dto.item_id)
            else:
                duplicate_items_list.append(item_dto.item_id)

        empty_list = len(duplicate_items_list) == 0
        non_empty_list = not empty_list

        missed_items = not len(items_list) == len(item_ids)
        missed_items_list = list(set(item_ids) - set(items_list))

        if non_empty_list:
            raise DuplicateItemsException(duplicate_items_list)

        elif missed_items:
            raise MissedItemsException(missed_items_list)


    @staticmethod
    def _validate_datetime(meal_datetime):
        invalid_datetime =  datetime.now() <= meal_datetime
        if invalid_datetime:
             raise InvalidTimeException
