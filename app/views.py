from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request,'login.html')
def home(request):
    return render(request,'home.html')
def car(request):
    return render(request,'car.html')
def bike(request):
    return render(request,'bike.html')
