from django.db import models
# from resource_management.constants.enums \
#     import AccessLevel, RequestStatus


class User(models.Model):
    name = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
