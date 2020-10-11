
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination
# Create your views here.


def index(request):
    dests= Destination.objects.all()
   # dest1 = Destination()
   # dest1.name = "Mumbai"
    # dest1.desc= 'The city that never sleeps!'
    # dest1.price = 700;
    # dest1.img = 'destination_1.jpg'
    # dest1.offer=False
    
    # dest2=Destination()
    # dest2.name = "Pune"
    # dest2.desc= 'The city of happiness!'
    # dest2.price = 500;
    # dest2.img = 'destination_2.jpg'
    # dest2.offer=True

    # dest3=Destination()
    # dest3.name = "Bangalore"
    # dest3.desc= 'The city of lakes!'
    # dest3.price = 900;
    # dest3.img = 'destination_3.jpg'
    # dest3.offer=False
    
    # dests= [dest1,dest2,dest3]


    
    
    return render(request, "index.html",{ 'dests' : dests})
