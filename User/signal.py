# from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Users, Profile


@receiver(post_save, sender=Profile)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Users.objects.create(user=instance)
