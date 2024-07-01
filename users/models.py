from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=250)
    year = models.CharField(max_length=250)
    parent = models.OneToOneField(User, on_delete=models.CASCADE)
    attend_date = models.DateField()