from django.db import models


# Create your models here.
class Media(models.Model):
    S_QUEUE = 0
    S_PLAYING = 1
    S_CANCELED = 2
    S_FINISHED = 3

    STATUS = [
        (S_QUEUE, "Esperando"),
        (S_PLAYING, "Tocando"),
        (S_CANCELED, "Cancelado"),
        (S_FINISHED, "Finalizado")
    ]

    order = models.IntegerField()
    name = models.CharField(max_length=256)
    file_path = models.TextField()
    file_type = models.CharField(max_length=10)
    status = models.IntegerField(choices=STATUS, default=S_QUEUE)
