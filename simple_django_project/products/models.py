from django.db import models

# Create your models here.

class Vine_Year(models.Model):
    value = models.CharField(max_length=50)
    is_user =models.BooleanField(default=True)


class Pizza_Size(models.Model):
    value = models.CharField(max_length=50)
    is_user =models.BooleanField(default=True)
    
class Vine(models.Model):
    name = models.CharField(max_length=100)
    year = models.ForeignKey(Vine_Year,on_delete=models.CASCADE,null=True)

class Pizza(models.Model):
    name = models.CharField(max_length=100)
    size = models.ForeignKey(Pizza_Size,on_delete=models.CASCADE,null=True)
