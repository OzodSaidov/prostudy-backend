from django.db import models

from prostudy.base_models import Base

class Region(Base):
    text = models.JSONField(default=dict)

    class Meta:
        ordering = ['text']

    @property
    def get_value(self):
        return self.text['en']

    def __str__(self):
        return self.text['en']

