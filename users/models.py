from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=250)
    parent = models.ForeignKey(User, on_delete=models.DO_NOTHING)


class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    parent = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=250)
    attended_at = models.DateTimeField()
    
    
class ResponseNotes(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    notes = models.TextField()
    date_submitted = models.DateTimeField()
    
class InquireNotes(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    notes = models.TextField()
    date_submitted = models.DateTimeField()