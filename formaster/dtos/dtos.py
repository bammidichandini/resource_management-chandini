from dataclasses import dataclass


@dataclass
class FormDto:
    form_id: int
    is_alive: bool

@dataclass
class UserResponseDto:
    user_id: int
    question_id: int
    user_option: int

@dataclass
class FibResponseDto:
    user_id: int
    question_id: int
    user_option: str
