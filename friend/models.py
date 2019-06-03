from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class friend(models.Model):
    to_user = models.ForeignKey(related_name='to_user')
    from_user = models.ForeignKey(related_name='from_user')


