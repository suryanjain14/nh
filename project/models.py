from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Project(models.Model):
    name = models.TextField(max_length=20)
    data = models .TextField()
    level = models.TextField(max_length=20)
    tag = models.TextField(max_length=20, null=True)
    #timestamp = models.PositiveSmallIntegerField(default=1, max_length='2')

    def __str__(self):
        return self.name


class Userpro(models.Model):
    user = models.ManyToManyField(User)
    current_project = models.ForeignKey(Project, on_delete=models.CASCADE)


class Userprodetal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    completion = models.BooleanField(default=False)


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
