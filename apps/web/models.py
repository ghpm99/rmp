from django.db import models


# Create your models here.
class Youtube(models.Model):
    order = models.IntegerField()
    name = models.CharField(max_length=100)
    url_path = models.TextField()
