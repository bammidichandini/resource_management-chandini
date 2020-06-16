from typing import List

class InvalidMealId(Exception):
    pass


class InvalidItemId(Exception):
    def __init__(
        self,
        items_list: List[int]
    ):
        self.items_list = items_list


class InvalidQuantity(Exception):
    def __init__(
        self,
        items_list: List[int]
    ):
        self.items_list = items_list



class DuplicateItemsException(Exception):
    def __init__(
        self,
        items_list: List[int]
    ):
        self.items_list = items_list


class MissedItemsException(Exception):
    def __init__(
        self,
        items_list: List[int]
    ):
        self.items_list = items_list


class InvalidTimeException(Exception):
    pass

class NoItemId(Exception):
    def __init__(
        self,
        items_list: List[int]
    ):
        self.items_list = items_list
