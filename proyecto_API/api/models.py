from msilib.schema import Class
from unittest.util import _MAX_LENGTH
from django.db import models


# Create your models here.
class Estudiante(models.Model):
    name=models.CharField(max_length=250)
    last_name=models.CharField(max_length=250)
    email=models.CharField(max_length=250)
    CI=models.CharField(max_length=250)
    parcial1=models.CharField(max_length=5)
    parcial2=models.CharField(max_length=5)
    parcial3=models.CharField(max_length=5)
    parcial4=models.CharField(max_length=5)
    promedio=models.CharField(max_length=5)


