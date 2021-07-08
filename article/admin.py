from django.contrib import admin
from article.models import *
from .forms import ArticleForm


class ArticleAdmin(admin.ModelAdmin):
    form = ArticleForm
    list_display = ('id', 'title', 'author', 'created_at', 'updated_at')


admin.site.register(Article, ArticleAdmin)
admin.site.register(Author)
