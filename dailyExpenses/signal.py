from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from dailyExpenses.models import Child


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Child.objects.create(user=instance)
