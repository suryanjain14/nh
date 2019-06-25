from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Groups(models.Model):
    name  = models.CharField(max_length=25)
    user1 = models.ManyToManyField(User,null=True)
    user2 = models.ManyToManyField(User,null=True)
    user3 = models.ManyToManyField(User,null=True)
    user4 = models.ManyToManyField(User,null=True)
    user5 = models.ManyToManyField(User,null=True)
    bio   = models.TextField(max_length=250,null=True)

