import pytest
from django_swagger_utils.drf_server.exceptions import Forbidden
from resource_management.exceptions.exceptions import UserCannotManipulateException
from resource_management.presenters.authentication_presenter import PresenterImplementation


def test_raise_user_cannot_manipulate_exception():

    #arrange

    presenter = PresenterImplementation()

    #act

    with pytest.raises(Forbidden):
        presenter.raise_user_cannot_manipulate_exception()
