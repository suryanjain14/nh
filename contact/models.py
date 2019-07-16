from django.db import models

class msg (models.Model):
    message=models.TextField()

class msguser (models.Model):
    msgusername = models.CharField (max_length=100,blank=True)
    email=models.EmailField (max_length=100)
