import pytest
from datetime import datetime
from food_management.dtos.dtos import MealItemDto
from freezegun import freeze_time
from unittest.mock import create_autospec
from food_management.exceptions.exceptions import (
    InvalidMealId,
    InvalidItemId,
    InvalidQuantity
    )
from django_swagger_utils.drf_server.exceptions import NotFound
from food_management.interactors.storages.storage_interface import StorageInterface
from food_management.interactors.presenters.presenter_interface import PresenterInterface
from food_management.interactors.create_user_preference_interactor import CreateUserPreference


def test_create_user_preference_with_invalid_meal_id():

    # arrange

    user_id = 1
    meal_id = 1
    items_dto_list = [MealItemDto(
            item_id = 1,
            quantity = 2
        )]

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    storage.validate_meal_id.side_effect = InvalidMealId
    presenter.raise_invalid_meal_id.side_effect = NotFound

    wrapper = CreateUserPreference(
        storage=storage,
        presenter=presenter
    )

    # act
    with pytest.raises(NotFound):
        wrapper.create_user_preference_wrapper(
            user_id=user_id,
            meal_id=meal_id,
            items_list_dto=items_dto_list
        )

    # assert
    storage.validate_meal_id.assert_called_once_with(meal_id=meal_id)
    presenter.raise_invalid_meal_id.assert_called_once()


def test_create_user_preference_with_invalid_item_id():

    # arrange

    user_id = 1
    meal_id = 1
    items_dto_list = [
        MealItemDto(
            item_id = 1,
            quantity = 2
        ),
        MealItemDto(
            item_id = 100,
            quantity = 2
        )
        ]
    item_ids_list = [1,2,3,4]
    items_list = [100]

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    presenter.raise_invalid_item_id.side_effect = NotFound
    storage.get_meal_items_ids.return_value = item_ids_list

    wrapper = CreateUserPreference(
        storage=storage,
        presenter=presenter
    )

    # act
    with pytest.raises(NotFound):
        wrapper.create_user_preference_wrapper(
            user_id=user_id,
            meal_id=meal_id,
            items_list_dto=items_dto_list
        )

    # assert
    storage.get_meal_items_ids.assert_called_once_with(meal_id=meal_id)
    error_class = presenter.raise_invalid_item_id.call_args.kwargs
    list_ids = error_class['error'].items_list
    assert list_ids == items_list


def test_create_user_preference_with_invalid_quantity():

    # arrange

    user_id = 1
    meal_id = 1
    items_dto_list = [MealItemDto(
            item_id=1,
            quantity=-1
        ),
        MealItemDto(
            item_id=2,
            quantity=2
        )
        ]
    item_ids_list = [1,2,3,4]
    items_list = [1]

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    presenter.raise_invalid_quantity.side_effect = NotFound
    storage.get_meal_items_ids.return_value = item_ids_list

    wrapper = CreateUserPreference(
        storage=storage,
        presenter=presenter
    )

    # act
    with pytest.raises(NotFound):
        wrapper.create_user_preference_wrapper(
            user_id=user_id,
            meal_id=meal_id,
            items_list_dto=items_dto_list
        )

    # assert
    storage.get_meal_items_ids.assert_called_once_with(meal_id=meal_id)
    error_class = presenter.raise_invalid_quantity.call_args.kwargs
    list_ids = error_class['error'].items_list
    assert list_ids == items_list



def test_create_user_preference_with_duplicate_items():

    # arrange

    user_id = 1
    meal_id = 1
    items_dto_list = [MealItemDto(
            item_id=1,
            quantity=2
        ),
        MealItemDto(
            item_id=1,
            quantity=2
        )
        ]
    item_ids_list = [1,2,3,4]
    items_list = [1]

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    presenter.raise_duplicate_items.side_effect = NotFound
    storage.get_meal_items_ids.return_value = item_ids_list

    wrapper = CreateUserPreference(
        storage=storage,
        presenter=presenter
    )

    # act
    with pytest.raises(NotFound):
        wrapper.create_user_preference_wrapper(
            user_id=user_id,
            meal_id=meal_id,
            items_list_dto=items_dto_list
        )

    # assert
    storage.get_meal_items_ids.assert_called_once_with(meal_id=meal_id)
    error_class = presenter.raise_duplicate_items.call_args.kwargs
    list_ids = error_class['error'].items_list
    assert list_ids == items_list



def test_create_user_preference_with_missed_items():

    # arrange

    user_id = 1
    meal_id = 1
    items_dto_list = [MealItemDto(
            item_id=1,
            quantity=2
        ),
        MealItemDto(
            item_id=2,
            quantity=2
        )
        ]
    item_ids_list = [1,2,3,4]
    items_list = [3,4]

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    presenter.raise_missed_items.side_effect = NotFound
    storage.get_meal_items_ids.return_value = item_ids_list

    wrapper = CreateUserPreference(
        storage=storage,
        presenter=presenter
    )

    # act
    with pytest.raises(NotFound):
        wrapper.create_user_preference_wrapper(
            user_id=user_id,
            meal_id=meal_id,
            items_list_dto=items_dto_list
        )

    # assert
    storage.get_meal_items_ids.assert_called_once_with(meal_id=meal_id)
    error_class = presenter.raise_missed_items.call_args.kwargs
    list_ids = error_class['error'].items_list
    assert list_ids == items_list


@freeze_time("2020-06-16")
def test_create_user_preference_to_update():

    # arrange

    user_id = 1
    meal_id = 1
    items_dto_list = [MealItemDto(
            item_id=1,
            quantity=2
        ),
        MealItemDto(
            item_id=2,
            quantity=2
        ),
        MealItemDto(
            item_id=3,
            quantity=2
        )
        ]
    item_ids_list = [1,2,3]

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    storage.get_meal_items_ids.return_value = item_ids_list
    storage.check_for_user_with_meal_id.return_value = True
    storage.get_datetime_object_to_meal.return_value = datetime(2020, 6, 1)

    wrapper = CreateUserPreference(
        storage=storage,
        presenter=presenter
    )

    # act

    wrapper.create_user_preference_wrapper(
            user_id=user_id,
            meal_id=meal_id,
            items_list_dto=items_dto_list
        )

    # assert
    storage.get_meal_items_ids.assert_called_once_with(meal_id=meal_id)
    storage.check_for_user_with_meal_id.assert_called_once_with(
        user_id=user_id,
        meal_id=meal_id
    )
    storage.update_the_meal.assert_called_once_with(
        user_id=user_id,
        meal_id=meal_id,
        items_list_dto=items_dto_list
    )
    storage.get_datetime_object_to_meal.assert_called_once_with(meal_id)


@freeze_time("2020-06-16")
def test_create_user_preference_to_create_user_preference():

    # arrange

    user_id = 1
    meal_id = 1
    items_dto_list = [MealItemDto(
            item_id=1,
            quantity=2
        ),
        MealItemDto(
            item_id=2,
            quantity=2
        ),
        MealItemDto(
            item_id=3,
            quantity=2
        )
        ]
    item_ids_list = [1,2,3]

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    storage.get_meal_items_ids.return_value = item_ids_list
    storage.check_for_user_with_meal_id.return_value = False
    storage.get_datetime_object_to_meal.return_value = datetime(2020, 5, 1)

    wrapper = CreateUserPreference(
        storage=storage,
        presenter=presenter
    )

    # act

    wrapper.create_user_preference_wrapper(
            user_id=user_id,
            meal_id=meal_id,
            items_list_dto=items_dto_list
        )

    # assert
    storage.get_meal_items_ids.assert_called_once_with(meal_id=meal_id)
    storage.check_for_user_with_meal_id.assert_called_once_with(
        user_id=user_id,
        meal_id=meal_id
    )
    storage.create_the_meal.assert_called_once_with(
        user_id=user_id,
        meal_id=meal_id,
        items_list_dto=items_dto_list
    )
    storage.get_datetime_object_to_meal.assert_called_once_with(meal_id)


@freeze_time("2020-06-16")
def test_create_user_preference_with_invalid_time():

    # arrange

    user_id = 1
    meal_id = 1
    items_dto_list = [MealItemDto(
            item_id=1,
            quantity=2
        ),
        MealItemDto(
            item_id=2,
            quantity=2
        ),
        MealItemDto(
            item_id=3,
            quantity=2
        )
        ]
    item_ids_list = [1,2,3]

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    storage.get_meal_items_ids.return_value = item_ids_list
    storage.check_for_user_with_meal_id.return_value = False
    storage.get_datetime_object_to_meal.return_value = datetime(2020, 6, 17)
    presenter.raise_invalid_time.side_effect = NotFound

    wrapper = CreateUserPreference(
        storage=storage,
        presenter=presenter
    )

    # act
    with pytest.raises(NotFound):
        wrapper.create_user_preference_wrapper(
                user_id=user_id,
                meal_id=meal_id,
                items_list_dto=items_dto_list
            )

    # assert
    storage.get_meal_items_ids.assert_called_once_with(meal_id=meal_id)
    # storage.check_for_user_with_meal_id.assert_called_once_with(
    #     user_id=user_id,
    #     meal_id=meal_id
    # )
    storage.get_datetime_object_to_meal.assert_called_once_with(meal_id)
