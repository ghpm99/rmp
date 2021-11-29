from django.db import models


# Create your models here.
class Media(models.Model):
    order = models.IntegerField()
    name = models.CharField(max_length=256)
    file_path = models.TextField()
    file_type = models.CharField(max_length=10)
    playing = models.BooleanField()
