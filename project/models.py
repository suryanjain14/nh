from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Project(models.Model):
    # this model defines the project details
    name = models.TextField(max_length=20)
    data = models .TextField()
    level = models.TextField(max_length=20)
    tag = models.TextField(max_length=20, null=True)
    #timestamp = models.PositiveSmallIntegerField(default=1, max_length='2')

    def __str__(self):
        return self.name


class Userpro(models.Model):
    # this model define just many to many relationship of user with project

    user = models.ManyToManyField(User)
    current_project = models.ForeignKey(Project, on_delete=models.CASCADE)


class Userprodetal(models.Model):
    # this model define the details of prject given to a particular user like how much project user has completed
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    completion = models.IntegerField(default=0)


#now we have to buid the logic for these models like that of friends

'''
    @classmethod
    def start_project(cls, current_project, user):
        project, created = cls.objects.get_or_create(
            current_project=current_project
        )
        Userpro.users.add(user)

    
'''
