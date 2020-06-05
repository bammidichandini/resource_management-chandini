from resource_management.presenters.authentication_presenter import PresenterImplementation



def test_get_login_response(user_auth_tokens_dto,
                            get_login_response):

    #arrange
    expected_dto = get_login_response
    presenter = PresenterImplementation()

    #act
    actual_dict = presenter.get_login_response(
        user_auth_tokens_dto
        )

    #assert
    assert actual_dict["user_id"] == expected_dto["user_id"]
    assert actual_dict["access_token"] == expected_dto["access_token"]
    assert actual_dict["refresh_token"] == expected_dto["refresh_token"]
    assert actual_dict["expires_in"] == expected_dto["expires_in"]