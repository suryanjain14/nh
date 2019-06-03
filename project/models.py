from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class project(models.Model):
    name = models.TextField(max_length=20)
    data = models .TextField()
    level = models.TextField(max_length=20)
    


class ugp(models.Model):
    uid =models.ManyToManyField(related_name=User)
    pid =models.ManyToManyField(related_name=project)