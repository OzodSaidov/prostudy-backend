from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from article import models


class ArticleForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = models.Article
        fields = '__all__'
