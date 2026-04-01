from django.db import models

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


class UseCase(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    


class Orders(models.Model):
    pass

class AddCart(models.Model):
    pass


