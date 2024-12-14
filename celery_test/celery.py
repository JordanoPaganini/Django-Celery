import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_test.settings')

from django.conf import settings

app = Celery('celery_test')
app.config_from_object(f'django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()