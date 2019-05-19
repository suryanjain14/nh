from django.db import models

# Create your models here.

class user(models.Model):
    name = models.TextField(max_length=40)
    email = models.TextField(max_length=30)
    city = models.TextField(max_length=20)
    country =models.TextField(max_length=20)
    gender=models.BooleanField()