from django.db import models
from django.db.models import IntegerField

# Create your models here.

from django.db import models

class Car(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    color = models.CharField(max_length=50)
    discriptions = models.TextField()
    image = models.ImageField(upload_to='cars/')
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Favorite(models.Model):

    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.car.name