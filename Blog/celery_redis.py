from __future__ import absolute_import, unicode_literals
from celery import Celery
from django.conf import settings
import os


# установка настроек django по умолчанию
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'siteblog.settings')

app = Celery('siteblog')

app.config_from_object('django.conf:settings')
app.conf.broker_url = settings.CELERY_BROKER_URL

# загрузка модулей задач из всех зареганых конфигов django
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'publishing_posts-every-minute': {
        'task': 'blog.task.publishing_posts',
        'schedule': 60.0
    } 
}
