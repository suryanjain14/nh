from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify




class Project(models.Model):
    # this model defines the project details
    name = models.TextField(max_length=20, unique=True)
    data = models .TextField()
    level = models.TextField(max_length=20)
    #timestamp = models.PositiveSmallIntegerField(default=1, max_length='2')

    def __str__(self):
        return self.name


class ProTags(models.Model):
    # this model store the tags of projects
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    tag = models.CharField(max_length=16)

    def __str__(self):
        return f'{self.project}'



@receiver(post_save, sender=Project)
def create_protags(sender, instance, created, **kwargs):
    if created:
        ProTags.objects.create(user=instance)


@receiver(post_save, sender=Project)
def save_protags(sender, instance, **kwargs):
    instance.ProTags.save()



class Userpro(models.Model):
    # this model define just many to many relationship of user

    project = models.ManyToManyField(Project)
    current_user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)


    # now we have to buid the logic for these models like that of friends
    @classmethod
    def start_project(cls, current_user, new_project):
        projectobj, created = cls.objects.get_or_create(
            current_user=current_user
        )
        projectobj.project.add(new_project)

    def __str__(self):
        return f'{self.current_user} projects'


class Pro_stat(models.Model):
    # ye model complete karne ke liye signals ki zaroorat pade gi this models stores whtat is the conditions of user for a project
    # model complete hai bas signal ke through is mai parameters bhejne hai ki jai se hi koi project start karthai
    # to us  user  pk aur project ki pk is mai save ho jye
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    completion = models.IntegerField(default=25)

    class Meta:
        unique_together = (("user", "project"),)

    def __str__(self):
        return f'{self.user}_{self.project}_stat'




'''
bhai log ek signal banana hai jo ki new project start karne par matlab 
userpro mai save() ya many to many field ke change hone par active ho
aur Pro_stat ke models mai user aur project ke column mai data dale
'''

'''
'''
class Project1(models.Model):
    pro_name=models.CharField(max_length=30)
    prerequisite=models.TextField()
    description=models.TextField()
    created_on=models.DateTimeField(auto_now_add=True)
    created_by=models.CharField(max_length=30,blank=True)
    duration = models.IntegerField(blank=True)
    slug = models.SlugField(max_length=30,blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.pro_name)
        super(Project1, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.pro_name}'


class UserPro1(models.Model):
    project = models.ForeignKey(Project1, on_delete=models.SET_NULL, null=True)
    admin = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    started_on = models.DateTimeField(auto_now_add=True, )
    users = models.ManyToManyField(User, related_name="users", null=True, default=admin)

    def __str__(self):
        return f'{self.admin} {self.project}'
