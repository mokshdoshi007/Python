from django.db import models
from myapp.models import Users
from django.contrib.postgres.fields import ArrayField

class Turfs(models.Model):
    DEFAULT_ID=1
    id=models.AutoField(primary_key=True)
    user=models.ForeignKey(Users, default=1, on_delete=models.SET_DEFAULT)
    name=models.CharField(max_length=50)
    capacity=models.IntegerField()
    description=models.CharField(max_length=1000)
    stars=models.FloatField(default=0)
    users=models.IntegerField(default=0)
    rate=models.IntegerField()
    imageUrls=ArrayField(models.URLField())
    contact=ArrayField(models.IntegerField(),null=True, blank=True)
    price=ArrayField(ArrayField(models.FloatField()), null=True, blank=True)
    slots=ArrayField(ArrayField(models.CharField(max_length=20)), null=True, blank=True)
    sourceprice=ArrayField(ArrayField(models.FloatField()), null=True, blank=True)
    sourceslots=ArrayField(ArrayField(models.CharField(max_length=20)), null=True, blank=True)

class Location(models.Model):
    turf=models.OneToOneField(Turfs, default=1, on_delete=models.SET_DEFAULT, primary_key=True)
    latitude=models.FloatField()
    longitude=models.FloatField()
    address=models.CharField(max_length=100)
    area=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    pincode=models.IntegerField()

class Bookings(models.Model):
    turf=models.ForeignKey(Turfs, default=1, on_delete=models.SET_DEFAULT)
    user=models.ForeignKey(Users, default=1, on_delete=models.SET_DEFAULT)
    date=models.DateField()
    slot=models.CharField(max_length=20)
    time=models.DateTimeField(auto_now_add=True, editable=False)