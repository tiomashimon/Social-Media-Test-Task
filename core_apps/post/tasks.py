from main.celery import app
from .models import DailyLikes
from django.utils import timezone


@app.task
def create_daily_likes():
    now = timezone.now()

    daily_likes_obj = DailyLikes.objects.create(date=now)