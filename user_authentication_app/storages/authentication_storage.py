from user_authentication_app.interactors.storage_interfaces.storage_interface import \
    StorageInterface


class StorageImplementation(StorageInterface):

    def validate_username(self, username: str):
        # try:
        #     User.objects.get(username=username)
        # except User.DoesNotExist:
        pass



    def validate_password(self, password: str, username: str):
        pass

    def is_admin(self, user_id: int) -> bool:
        pass
