from django.db import models
from django.contrib.auth.models import User

# Create your models here.
PROMOTER = (
    (True, "Admin"),
    (False, "User"),
)
LANG = (
    ("Python", "Python"),
    ("Java", "Java"),
    ("CFamily", "CFamily"),
    ("JavaScript", "JavaScript"),

)


class Language(models.Model):
    language = models.CharField(max_length=10, choices=LANG)
    description = models.TextField(max_length=8042, default="")

    def __str__(self):
        return f'{self.language}'


class Reslink(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    slug = models.SlugField(unique=True)
    time = models.DateTimeField(auto_now=True)
    description = models.TextField(max_length=1024)
    links = models.URLField()
    creator = models.ForeignKey(to=User, on_delete=models.DO_NOTHING)
    promoter = models.BooleanField(default=False, choices=PROMOTER)

    def __str__(self):
        return f'{self.name}'


class Resofile(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    slug = models.SlugField(unique=True)
    time = models.DateTimeField(auto_now=True)
    description = models.TextField(max_length=1024)
    files = models.FileField(upload_to='media/resources/img')
    creator = models.ForeignKey(to=User, on_delete=models.DO_NOTHING)
    promoter = models.BooleanField(default=False, choices=PROMOTER)

    def __str__(self):
        return f'{self.name}'


class Resoimg(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    slug = models.SlugField(unique=True, null=True)
    time = models.DateTimeField(auto_now=True)
    description = models.TextField(max_length=1024)
    image = models.ImageField(upload_to='media/resources/img')
    creator = models.ForeignKey(to=User, on_delete=models.DO_NOTHING)
    promoter = models.BooleanField(default=False, choices=PROMOTER)

    def __str__(self):
        return f'{self.name}'


class Resource_Platform_img(models.Model):
    resources = models.ForeignKey(Resoimg, on_delete=models.CASCADE)
    tags = models.CharField(max_length=25)

    def __str__(self):
        return f'{self.resources} {self.tags}'


class Resource_Platform_link(models.Model):
    resources = models.ForeignKey(Reslink, on_delete=models.CASCADE)
    tags = models.CharField(max_length=25)

    def __str__(self):
        return f'{self.resources} {self.tags}'


class Resource_Platform_file(models.Model):
    resources = models.ForeignKey(Resofile, on_delete=models.CASCADE)
    tags = models.CharField(max_length=25)

    def __str__(self):
        return f'{self.resources} {self.tags}'
