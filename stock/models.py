from operator import mod
from pyexpat import model
from django.db import models

# Create your models here.
class Stock(models.Model):
    date = models.DateField()
    trade_code = models.CharField(max_length=300)
    high = models.FloatField()
    low = models.FloatField()
    open = models.FloatField()
    close = models.FloatField()
    volume = models.IntegerField()