from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.utils import timezone


from .models import UserActivity


@receiver(post_save, sender=User)
def create_user_activity(sender, instance, created,**kwargs):
    if created:
        UserActivity.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_activity(sender, instance, created,**kwargs):
    if created:
        user_activity = instance.useractivity.save(commit=False)
        user_activity.last_request_time  = timezone.now()