from django.db import models
from django.contrib.auth.models import User # it is for the orders model

# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=50)
    price = models.IntegerField()
    mileage = models.FloatField()
    seating = models.IntegerField()
    fuel_type = models.CharField(max_length=20)
    transmission = models.CharField(max_length=20)
    horsepower = models.IntegerField()
    body_type = models.CharField(max_length=20)
    description = models.TextField()
    image = models.ImageField(upload_to='cars/')

    def __str__(self):
        return self.name


class UseCase(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    total_price = models.IntegerField()
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled')
    ], default='pending')

    created_at = models.DateTimeField(auto_now_add=True)


class AddCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)
