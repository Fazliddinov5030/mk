import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'book.settings')

app = Celery('book')
app.config_from_object('django.conf:settings', namespace='CELERY')

# Loyihadagi barcha tasks.py fayllarini avtomatik qidirib topadi
app.autodiscover_tasks()

# Celery Beat orqali obunalarni har kuni tekshirib turish
app.conf.beat_schedule = {
    'deactivate-expired-subscriptions-daily': {
        'task': 'book.tasks.cancel_expired_subscriptions',
        'schedule': crontab(hour=0, minute=0),  # Har kuni kechasi 00:00 da ishlaydi
    },
}