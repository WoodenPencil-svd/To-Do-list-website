from django.contrib import admin
from source.models import *
from django.contrib.auth.models import  Permission
from django.contrib.contenttypes.models import ContentType
# Register your models here.
admin.site.register(Task)
admin.site.register(CustomUser)
admin.site.register(Permission)
admin.site.register(ContentType)