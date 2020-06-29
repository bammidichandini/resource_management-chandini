from django.db import models


class Resource(models.Model):
    image_url = models.URLField(max_length=200)
    name = models.CharField(max_length=50,unique=True)
    item_name = models.CharField(max_length=50)
    link = models.URLField(max_length=200)
    description = models.CharField(max_length=50)