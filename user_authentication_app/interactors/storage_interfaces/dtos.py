from dataclasses import dataclass


@dataclass()
class UserDTO:
    user_id: int
    name: str
    profile_pic: str
    username: str
    password: str
    is_admin : bool
