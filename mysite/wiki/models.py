import datetime

from django.db import models
from django.utils import timezone


class Page(models.Model):
    title = models.CharField(max_length=64, primary_key=True)
    content = models.TextField()

    def __str__(self):
        return self.title
