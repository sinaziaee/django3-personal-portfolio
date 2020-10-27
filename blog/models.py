from django.db import models
from django.utils import timezone


class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    date = models.DateField(default=timezone.now)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title
