from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Project(models.Model):
    name = models.TextField(max_length=20)
    data = models .TextField()
    level = models.TextField(max_length=20)
    tag = models.TextField(max_length=20, null=True)
    #timestamp = models.PositiveSmallIntegerField(default=1, max_length='2')


class Userpro(models.Model):
    project = models.ManyToManyField(User)
    current_project = models.ForeignKey(Project, on_delete=models.CASCADE)


'''
    @classmethod
    def start_project(cls, current_project, new_friend):
        project, created = cls.objects.get_or_create(
            current_project=current_project
        )
        Userpro.users.add(new_friend)

    @classmethod
    def finish_project(cls, current_user, new_friend):
        project, created = cls.objects.get_or_create(
            current_user=current_user
        )
        project.users.remove(new_friend)
'''


class ProUser(models.Model):
    completion = models.IntegerField()
