import pytest
from resource_management.presenters.authentication_presenter import PresenterImplementation
from resource_management.exceptions.exceptions import InvalidUserException


def test_raise_invaalid_exception():

    #arrange

    presenter = PresenterImplementation()

    #act
    with pytest.raises(InvalidUserException):
        presenter.raise_invalid_username_exception()

