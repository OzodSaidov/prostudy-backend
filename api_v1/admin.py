from django_json_widget.widgets import JSONEditorWidget
from django.contrib import admin
from django.db import models
from api_v1 import models as api_models


# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.JSONField: {'widget': JSONEditorWidget},
    }


admin.site.register(api_models.Course, CourseAdmin)
