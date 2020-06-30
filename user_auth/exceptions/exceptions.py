from typing import List


class InvalidUserException(Exception):
    pass


class InvalidPasswordException(Exception):
    pass


class InvalidIdException(Exception):
    def __init__(self, user_ids: List[int]):
        self.user_ids = user_ids
