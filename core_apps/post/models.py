from django.db import models
from django.contrib.auth.models import User
from ..user.models import UserProfile


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)
    created_by = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)


class DailyLikes(models.Model):
    date = models.DateField(unique=True)
    likes_count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.date} - {self.likes_count} likes"
    


