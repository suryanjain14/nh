from django.contrib.auth.models import User
from django.db.models.signals import  post_save
from django.dispatch import receiver
from django.db import models

# Create your models here.
class Notification(models.Model):
    title = models.CharField(max_length=50)
    message = models.TextField()
    viewed = models.BooleanField(default=false)
    user = models.ForeignKey(User)

@receiver(post_save, sender= User)
def collab_request(sender, **kwargs):
    if kwargs.get('created', False):
        Notification.objects.create(user=kwargs.get('instance'),
                                    title = (),
                                    message = ())