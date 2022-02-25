from asyncio import events
from django.db import models

# Create your models here.


class Book(models.Model):
    firstname=models.CharField(max_length=25)
    lastname=models.CharField(max_length=25)
    email=models.EmailField()
    phone=models.CharField(max_length=25)
    gender=models.CharField(max_length=25)
    age=models.CharField(max_length=25)
    event=models.CharField(max_length=25)
    venues=models.CharField(max_length=25)
    area=models.CharField(max_length=25)
    city=models.CharField(max_length=25)
    pincode=models.CharField(max_length=25)
    state=models.CharField(max_length=25)
    description=models.TextField()

    def __str__(self):
        return self.firstname