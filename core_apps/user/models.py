from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class UserActivity(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    last_request_time = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'UserActivity'
        verbose_name_plural = 'UserActivity'

    def __str__(self):
        return self.user.username