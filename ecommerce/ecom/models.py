from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    address=models.CharField(max_length=100)
    mobile=models.IntegerField()

class Department(models.Model):
    dep_name=models.CharField(max_length=100)
    dep_description=models.TextField()

class Student(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    date_of_birth=models.DateField()
    email=models.EmailField(unique=True)