from ib_common.service_adapter_utils.base_adapter_class import BaseAdapterClass


class ServiceAdapter(BaseAdapterClass):
    def __init__(self, *args, **kwargs):
        from django.conf import settings
        source = settings.IB_MINIPROJECTS_BACKEND_SOURCE
        kwargs['source'] = source
        super(ServiceAdapter, self).__init__(*args, **kwargs)

class ServicesAdapter:
    @property
    def auth_service(self):
        from .auth_service import AuthService
        return AuthService()


    # @property
    # def reactions_service(self):
    #     from .reactions_service import ReactionsService
    #     return ReactionsService()

def get_service_adapter():
    return ServicesAdapter()

    # ******* sample service adapter property ********
    # @property
    # def ib_users(self):
    #     from sample_app.adapters.ib_users_service_adapter import \
    #         IBUsersServiceAdapter
    #     return IBUsersServiceAdapter(access_token=self.access_token,
    #                                  user=self.user, source=self.source)
