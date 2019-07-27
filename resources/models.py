from django.db import models
from django.contrib.auth.models import User

# Create your models here.
PROMOTER = (
    (True, "Admin"),
    (False, "User"),
)


class Resources(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(unique=True)
    time = models.DateTimeField(auto_now=True)
    description = models.TextField(max_length=1024)
    image = models.ImageField(null=True)
    files = models.FileField(null=True)
    links = models.CharField(max_length=512, null=True)
    creator = models.ForeignKey(to=User, on_delete=models.DO_NOTHING)
    promoter = models.BooleanField(default=False, choices=PROMOTER)
    language = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.name}'


class Resource_Platform(models.Model):
    resources = models.ForeignKey(Resources, on_delete=models.CASCADE)
    tags = models.CharField(max_length=25)

    def __str__(self):
        return f'{self.resources} {self.tags}'
