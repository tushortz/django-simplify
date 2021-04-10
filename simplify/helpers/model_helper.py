from django.db import models
from django.utils import timezone


class TimeBasedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class NamedTimeBasedModel(TimeBasedModel):
    name = models.CharField(max_length=50)

    class Meta:
        abstract = True
        ordering = ['name']

    def __str__(self):
        return self.name