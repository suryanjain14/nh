from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models.signals import m2m_changed
from .models import Pro_stat, Userpro


@receiver(post_save, sender=Userpro)
def saveprostat(sender, **kwargs):
    Pro_stat.save()


@receiver(m2m_changed, sender=Userpro)
def saveprostat(sender, **kwargs):
    Pro_stat.save()


def send_pizza(self, toppings, size):
    pizza_done.send(sender=self.__class__, toppings=toppings, size=size)
