from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='ppic.jpg', upload_to='ppic/')
    city = models.CharField(max_length=20, null=True, default='Indore')
    country = models.CharField(max_length=20, null=True, default='Indiaa')
    college = models.CharField(max_length=20, null=True, default='IIPS')
    dob = models.DateField(max_length=20, null=True)
    bio = models.TextField(max_length=250, null=True)


    def __str__(self):

        return f'{self.user.username }profile'


class Friend(models.Model):
    users = models.ManyToManyField(to=User)
    current_user = models.ForeignKey(User, related_name='owner', on_delete=models.CASCADE, null=True)



    @classmethod
    def make_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users.add(new_friend)

    @classmethod
    def remove_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users.remove(new_friend)
