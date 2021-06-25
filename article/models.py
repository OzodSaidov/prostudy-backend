from django.db import models
from prostudy.base_model import Base


class Author(Base):
    name = models.CharField(max_length=255)
    email = models.EmailField()


class Article(Base):
    title = models.CharField(max_length=255)
    body = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='articles')
