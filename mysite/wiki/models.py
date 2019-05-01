import datetime

from django.db import models
from django.utils import timezone


class Page(models.Model):
    page_text = models.CharField(max_length=200)
    