from dataclasses import dataclass


@dataclass
class FormDto:
    form_id: int
    is_alive: bool
