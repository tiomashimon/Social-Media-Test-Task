from django.db import models
from django.contrib.auth.models import User
from ..user.models import UserActivity
from django.utils import timezone

class DailyLikes(models.Model):
    date = models.DateField(unique=True)
    likes_count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.date} - {self.likes_count} likes"



class Post(models.Model):

    title = models.CharField(max_length=255)
    content = models.TextField()
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)
    created_by = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)

    def like_unlike(self, user):
        daily_likes = DailyLikes.objects.get(date=timezone.now())
        response = ''
        if user in self.likes.all():
            self.likes.remove(user)
            response = 'Unlike'
            daily_likes.likes_count -= 1

        else:
            self.likes.add(user)
            response = 'Like'
            daily_likes.likes_count += 1
        daily_likes.save()
        return response


    


