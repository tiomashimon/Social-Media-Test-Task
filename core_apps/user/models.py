from django.db import models
from django.contrib.auth.models import User

class UserActivity(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    last_request_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.user.username