from abc import ABC
from abc import abstractmethod


class PresenterInterface(ABC):

    @abstractmethod
    def raise_form_does_not_exist_exception(self):
        pass

    @abstractmethod
    def raise_form_expired_exception(self):
        pass

    @abstractmethod
    def raise_invalid_question_id(self):
        pass
