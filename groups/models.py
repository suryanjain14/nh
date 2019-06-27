from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Groupdetails(models.Model):

    name = models.CharField(max_length=20, unique=True, null= True)
    bio = models.TextField(max_length=250, null=True)
    admin = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True )

    def __str__(self):
        return f'{self.name }'

class Usrgroup(models.Model):
    users = models.ManyToManyField(to=User, null=True)
    current_group = models.ForeignKey(to=Groupdetails,on_delete=models.CASCADE)
