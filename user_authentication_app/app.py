from django.apps import AppConfig


class UserAuthenticationAppAppConfig(AppConfig):
    name = "user_authentication_app"

    def ready(self):
        from user_authentication_app import signals # pylint: disable=unused-variable
