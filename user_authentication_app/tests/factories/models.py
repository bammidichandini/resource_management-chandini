from user_authentication_app.models import User
import factory


class UserModelFactory(factory.Factory):
    class Meta:
        model = User

    # user_id = factory.Sequence(lambda n: n)
    name = factory.Sequence(lambda n: "user %03d" % n)
    profile_pic = factory.Sequence(lambda n: "profile_pic %03d" % n)
    is_admin = factory.Iterator([True, False])
    username = factory.Sequence(lambda n: "username %03d" %n)
    password = factory.Sequence(lambda n: "password %03d" % n)