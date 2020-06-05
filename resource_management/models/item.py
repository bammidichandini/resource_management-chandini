from django.db import models
from resource_management.models import Resource, User
from resource_management.constants.enums \
    import AccessLevel, RequestStatus


class Item(models.Model):
    name = models.CharField(max_length=50)
    link = models.URLField(max_length=200)
    description = models.CharField(max_length=50)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    user = models.ManyToManyField(
        "User",
        through="UserAccess",
        related_name="user_access_level")


class UserAccess(models.Model):
    item = models.ForeignKey(Item,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    access_choices = (
        (AccessLevel.Read.value, AccessLevel.Read.value),
        (AccessLevel.Write.value, AccessLevel.Write.value),
        (AccessLevel.Read_and_Write.value, AccessLevel.Read_and_Write.value)
        )
    access_level = models.CharField(max_length=50, choices=access_choices,null=True)


class Request(models.Model):

    duration = models.DateTimeField(default=None,null=True)

    reason = models.CharField(max_length=200,default=None,null=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)

    status_choices = (
        (RequestStatus.Pending.value, RequestStatus.Pending.value),
        (RequestStatus.Accepted.value, RequestStatus.Accepted.value),
        (RequestStatus.Rejected.value, RequestStatus.Rejected.value)
        )
    status = models.CharField(max_length=50, default=RequestStatus.Pending.value,
                              choices=status_choices
                              )
    remarks = models.CharField(max_length=200,default=None,null=True)

    access_level = models.CharField(max_length=50, choices=access_choices,null=True)