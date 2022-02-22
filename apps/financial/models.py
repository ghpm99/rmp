from django.db import models


# Create your models here.
class Payment(models.Model):

    TYPE_CREDIT = 0
    TYPE_DEBIT = 1

    TYPES = [
        (TYPE_CREDIT, 'credit'),
        (TYPE_DEBIT, 'debit')
    ]

    type = models.IntegerField(default=TYPE_CREDIT, choices=TYPES)
    name = models.TextField(max_length=255)
    date = models.DateField()
    installments = models.IntegerField()
    payment_date = models.DateField()
    fixed = models.BooleanField()
    active = models.BooleanField(default=True)
    value = models.IntegerField(default=0)


class Month(models.Model):

    MONTH_EMPTY = 0
    MONTH_PROJECTION = 1
    MONTH_CALCULATED = 2
    MONTH_ACCOUNTED = 3

    STATUS = [
        (MONTH_EMPTY, 'empty'),
        (MONTH_PROJECTION, 'projection'),
        (MONTH_CALCULATED, 'calculated'),
        (MONTH_ACCOUNTED, 'accounted')
    ]
    status = models.IntegerField(default=MONTH_EMPTY, choices=STATUS)
    month = models.IntegerField()
    year = models.IntegerField()
    total = models.IntegerField()
