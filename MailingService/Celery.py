import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MailingService.settings')

app = Celery('MailingService')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'test-worker-lol': {
        'task': 'mail.tasks.send_mail',
        'schedule': crontab(minute='*/1'),
    }
}