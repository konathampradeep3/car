from django.shortcuts import render
from app.models import *
from django.http import HttpResponse

# Create your views here.
def login(request):
    return render(request,'login.html')
def home(request):
    return render(request,'home.html')
def car(request):
    return render(request,'car.html')
def bike(request):
    return render(request,'bike.html')



def insert_car(request):
    nm=input('enter car name')
    brd=input('enter brand of the car')
    pr=int(input('enter price'))
    seat=int(input('enter seaters'))
    mil=float(input('enter mileage'))
    ftype=input('enter fuel type')
    tras=input('enter transmission')
    hp=int(input('enter horse power'))
    bt=input('enter body type')
    desc=input('enter description')
    img=input('enter path')

    TCO=Car.objects.get_or_create(name=nm,brand=brd,price=pr,seating=seat,mileage=mil,fuel_type=ftype,transmission=tras,horsepower=hp,
                                  body_type=bt,description=desc,image=img)
    if TCO:
        return HttpResponse('object is created')
    else:
        return HttpResponse('already present')  



def display_car(request):
    QCO=Car.objects.all()

    d={'QCO':QCO}


    return render(request,'display_car.html',d)   









