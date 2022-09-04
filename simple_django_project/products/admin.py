from django.contrib import admin

from .models import Pizza,Vine,Vine_Year,Pizza_Size

# Register your models here.
admin.site.register(Vine_Year)
admin.site.register(Pizza_Size)
admin.site.register(Vine)
admin.site.register(Pizza)