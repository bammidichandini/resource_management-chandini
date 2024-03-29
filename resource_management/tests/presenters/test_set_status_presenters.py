import pytest
from resource_management.exceptions.exceptions import InvalidIdException
from resource_management.presenters.authentication_presenter import PresenterImplementation


def test_raise_invalid_id_exception():

    # arrange

    presenter = PresenterImplementation()

    # act

    with pytest.raises(InvalidIdException):
        presenter.raise_invalid_id_exception()

