from django.shortcuts import render
from .models import Hotel
# Create your views here.
def index(request):
    return render(request,'index.html')

def hotel(request):
    hotels = Hotel.objects.all()
    return render(request,'hotel.html',{'hotels':hotels})