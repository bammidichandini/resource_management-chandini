import pytest
from resource_management.exceptions.exceptions import \
        UserAlreadyExistedException
from resource_management.presenters.authentication_presenter \
        import PresenterImplementation


@pytest.mark.django_db
def test_raise_user_already_existed_exception():

    # arrange

    presenter = PresenterImplementation()

    # act
    with pytest.raises(UserAlreadyExistedException):
        presenter.raise_user_already_existed_exception()
