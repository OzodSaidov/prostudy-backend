from django import forms
from api_v1 import models
from django_json_widget.widgets import JSONEditorWidget


class JsonFiledForm(forms.ModelForm):
    class Meta:
        model = models.Course
        fields = ('title',)
        widgets = {
            'jsonfield': JSONEditorWidget
        }
