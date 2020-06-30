from django.contrib import admin
from resource_management.models import *
from resource_management.models.item import *


admin.site.register(Request)
admin.site.register(Item)
admin.site.register(UserAccess)
admin.site.register(Resource)
