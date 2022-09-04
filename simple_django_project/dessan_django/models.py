from django.db import models

# Create your models here.
class Hotel(models.Model):
    name = models.CharField(max_length=256)
    site_url = models.CharField(max_length=256)
    count_rings = models.IntegerField(name = "Количество звезд")
    count_rooms = models.IntegerField(name = "Количество комнат")
        
class Place(models.Model):
    name = models.CharField(max_length=256)
    is_open = models.BooleanField(default=True)
