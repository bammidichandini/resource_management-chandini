from user_authentication_app.interactors.presenter_interfaces.presenter_interface import \
    PresenterInterface
from user_authentication_app.interactors.presenter_interfaces.dtos import AccessTokenDTO
from django.http import response


class PresenterImplementation(PresenterInterface):

    def raise_invalid_user_exception(self):
        from user_authentication_app.constants.exception_messages import USER_DOES_NOT_EXIST
        import json
        response_object = response.HttpResponse(
            json.dumps({"response": USER_DOES_NOT_EXIST[0],
                        "http_status_code": 403,
                        "res_status": USER_DOES_NOT_EXIST[1]}), 403)
        return response_object


    def raise_invalid_password_exception(self):
        from user_authentication_app.constants.exception_messages import INVALID_PASSWORD
        import json
        response_object = response.HttpResponse(
            json.dumps({"response": INVALID_PASSWORD[0],
                        "http_status_code": 403,
                        "res_status": INVALID_PASSWORD[1]}), 403)
        return response_object


    def get_login_response(self, access_token_obj: AccessTokenDTO, is_admin: bool):
        response_dict = {
            "access_token": access_token_obj.access_token,
            "is_admin": is_admin
        }
        return response_dict