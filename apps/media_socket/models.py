from django.db import models


class Event(models.Model):
    event = models.CharField(max_length=30)
