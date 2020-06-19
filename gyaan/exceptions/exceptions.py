from typing import List


class InvalidDomainId(Exception):
    pass


class UserNotFollowing(Exception):
    pass


class InvalidPostIds(Exception):
    def __init__(self, post_ids: List[int]):
        self.post_ids = post_ids

class InvalidInput(Exception):
    pass
