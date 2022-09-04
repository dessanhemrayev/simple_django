from django.db import models
from products.models import Pizza,Vine
# Create your models here.
class Hotel(models.Model):
    name = models.CharField(max_length=256)
    site_url = models.CharField(max_length=256)
    count_rings = models.IntegerField(name = "Количество звезд")
    count_rooms = models.IntegerField(name = "Количество комнат")
    pizza = models.ManyToManyField(Pizza)
    vine = models.ManyToManyField(Vine)
    picture = models.ImageField(upload_to ='uploads/',null=True)
        
class Place(models.Model):
    name = models.CharField(max_length=256)
    is_open = models.BooleanField(default=True)
    hotel_id = models.ForeignKey(Hotel,null=True,on_delete=models.CASCADE)
