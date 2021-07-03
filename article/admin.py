from django.contrib import admin
from article.models import *


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'created_at', 'updated_at')


admin.site.register(Article, ArticleAdmin)
admin.site.register(Author)
