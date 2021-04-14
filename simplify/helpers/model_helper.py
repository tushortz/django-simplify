from django.db import models
from django.utils import timezone


class TimeBasedModel(models.Model):
    """Abstract model that can be inherited. it provides two fields for use. `created_at` and `updated_at`"""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class NamedTimeBasedModel(TimeBasedModel):
    """Abstract model that can be inherited. it provides three fields for use. `name`, `created_at` and `updated_at`"""

    name = models.CharField(max_length=50)

    class Meta:
        abstract = True
        ordering = ['name']

    def __str__(self):
        return self.name
