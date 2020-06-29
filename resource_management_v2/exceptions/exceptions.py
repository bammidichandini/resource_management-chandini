from typing import List


class InvalidUserException(Exception):
    pass


class InvalidPasswordException(Exception):
    pass


class UserCannotManipulateException(Exception):
    pass


class UserAlreadyExistedException(Exception):
    pass

class InvalidIdException(Exception):
    pass

class InvalidDetailsException(Exception):
    pass

class InvalidOffsetOrLimit(Exception):
    pass

class InvalidItemsException(Exception):
    def __init__(self, item_ids: List[int]):
        self.items_ids = item_ids
