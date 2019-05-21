from django.db import models

# Create your models here.
from django.contrib.auth.models import User
# Create your models here.



class profile(models.Model):
    user= models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='ppic.jpg',upload_to='ppic')
    city = models.CharField(max_length=20,null=True,default='Indore')
    country =models.CharField(max_length=20,null=True,default='India')
    college=models.CharField(max_length=20,null=True,default='IIPS')
    dob=models.DateField(max_length=20,null=True)

    def __str__(self):

        return f'{self.user.username } profile'


