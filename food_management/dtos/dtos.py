from dataclasses import dataclass


@dataclass
class MealItemDto:
    item_id: int
    quantity: int


# @dataclass
# class MealItemsDto:
#     user_id: int
#     meal_id: int
#     items_list: List[MealItemDto]
