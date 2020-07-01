import pytest
from resource_management.presenters.authentication_presenter import PresenterImplementation
from resource_management.exceptions.exceptions import InvalidPasswordException


def test_raise_invaalid_exception():

    #arrange

    presenter = PresenterImplementation()

    #act
    with pytest.raises(InvalidPasswordException):
        presenter.raise_invalid_password_exception()

