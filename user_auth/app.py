from django.apps import AppConfig


class UserAuthAppConfig(AppConfig):
    name = "user_auth"

    def ready(self):
        from user_auth import signals # pylint: disable=unused-variable
