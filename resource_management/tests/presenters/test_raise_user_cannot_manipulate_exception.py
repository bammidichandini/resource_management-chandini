import pytest
from resource_management.exceptions.exceptions import UserCannotManipulateException
from resource_management.presenters.authentication_presenter import PresenterImplementation


def test_raise_user_cannot_manipulate_exception():

    #arrange

    presenter = PresenterImplementation()

    #act

    with pytest.raises(UserCannotManipulateException):
        presenter.raise_user_cannot_manipulate_exception()
