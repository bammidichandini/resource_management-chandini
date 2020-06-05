import pytest
from resource_management.exceptions.exceptions import InvalidDetailsException
from resource_management.presenters.authentication_presenter import PresenterImplementation


def test_raise_invalid_details_exception():

    # arrange

    presenter = PresenterImplementation()

    # act

    with pytest.raises(InvalidDetailsException):
        presenter.raise_invalid_details_exception()
