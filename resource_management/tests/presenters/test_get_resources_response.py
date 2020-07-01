import pytest
from resource_management.presenters.authentication_presenter import PresenterImplementation


@pytest.mark.django_db()
def test_get_resource_repsonse(resource_dto,
                               get_resources_response
                              ):

    #arrange

    presenter = PresenterImplementation()

    #act

    actual_dto = presenter.get_resources_response(
        resources_dto_list=resource_dto
        )

    #assert
    assert actual_dto == get_resources_response