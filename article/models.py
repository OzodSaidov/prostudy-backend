from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from prostudy.base_model import Base


class Author(Base):
    name = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Article(Base):
    title = models.CharField(max_length=255)
    body = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='articles')

    def __str__(self):
        return self.title
