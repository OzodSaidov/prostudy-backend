from django.contrib import admin
from user.admin import BaseAdmin
from .models import Region

admin.site.register(Region, BaseAdmin)
