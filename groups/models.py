from django.db import models
from django.contrib.auth.models import User
from project.models import Project
# Create your models here.

STATUS = (
    (0, "Active"),
    (1, "Closed"),
)


class Group(models.Model):

    # This model stores the details of groups just like profile  of user
    name = models.CharField(max_length=20, unique=True, null= True)
    bio = models.TextField(max_length=250, null=True)
    admin = models.ForeignKey(to=User, on_delete=models.SET_NULL,related_name='User', null= True)
    entrykey = models.CharField(max_length=20, null=True)
    status = models.IntegerField(choices=STATUS, default=0)
    image = models.ImageField(default='gpic', upload_to='gpic/')
    users = models.ManyToManyField(User, blank=True, default=admin)
    project = models.ManyToManyField(Project, blank=True)

    def __str__(self):
        return f'{self.name }'


class GroupAdmin(models.Model):
    group = models.OneToOneField(Group, on_delete=models.CASCADE)
    admin = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


class Groupuser(models.Model):
    user = models.ManyToManyField(User)
    current_group = models.ForeignKey(Group, on_delete=models.CASCADE)


class Groupprojects(models.Model):
    project = models.ManyToManyField(Project)
    current_group = models.ForeignKey(Group, on_delete=models.CASCADE)



'''
class Usrgroup(models.Model):

    # this model combines the user and group it will define the many to many relationship between the group and user
    users = models.ManyToManyField(to=User)
    current_group = models.ForeignKey(to=Groupdetails,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.current_group }'


class Progroup(models.Model):

    # this model combines the project with the group
    project = models.ManyToManyField(Project)
    current_group = models.ForeignKey(to=Groupdetails, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.current_group }'

# now we have to buid the logic for these models
'''