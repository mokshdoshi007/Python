from django.db import models
from django.contrib.postgres.fields import ArrayField

class Users(models.Model):
    DEFAULT_PK=1
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    contact=models.BigIntegerField(unique=True)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=256)
    birthday=models.DateField(max_length=30)
    city=models.CharField(max_length=20, default="Mumbai")
    authToken=ArrayField(models.CharField(max_length=50),max_length=3)
    favturfs=ArrayField(models.IntegerField(), default=list, blank=True)
    stars=ArrayField(ArrayField(models.IntegerField()), default=list, blank=True)
    owner=models.BooleanField(default=False)

class TempUsers(models.Model):
    name=models.CharField(max_length=30)
    contact=models.BigIntegerField()
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=256)
    birthday=models.DateField(max_length=30)
    otp=models.IntegerField()