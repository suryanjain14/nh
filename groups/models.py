from django.db import models
from django.contrib.auth.models import User
from project.models import Project
# Create your models here.


class Groupdetails(models.Model):
    # This model stores the details of roups just like profile  of user
    name = models.CharField(max_length=20, unique=True, null= True)
    bio = models.TextField(max_length=250, null=True)
    admin = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True )

    def __str__(self):
        return f'{self.name }'


class Usrgroup(models.Model):
    # this model combines the user and group it will define the many to many relationship between the group and user
    users = models.ManyToManyField(to=User, null=True)
    current_group = models.ForeignKey(to=Groupdetails,on_delete=models.CASCADE)


class Progroup(models.Model):
    # this model combines the project with the group
    project = models.ManyToManyField(Project)
    current_group = models.ForeignKey(to=Groupdetails, on_delete=models.CASCADE)

# now we have to buid the logic for these models
