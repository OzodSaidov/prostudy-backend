from django.db import models


# Courses
class Course(models.Model):
    title = models.JSONField(default=dict)
