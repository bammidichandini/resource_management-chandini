from django.apps import AppConfig


class WashingAlotsAppAppConfig(AppConfig):
    name = "washing_alots_app"

    def ready(self):
        from washing_alots_app import signals # pylint: disable=unused-variable
