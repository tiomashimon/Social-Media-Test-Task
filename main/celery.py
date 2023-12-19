import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')


app = Celery('main')


app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


app.conf.beat_schedule = {
    'delete-expired-chats':
    {
        'task': 'core_apps.post.tasks.create_daily_likes',
        'schedule': crontab(minute=0, hour=0)
    }
}