import os
from celery import Celery
from datetime import timedelta
from decouple import config


# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
celery_app = Celery('config')

# celery_app.config_from_object('django.conf:settings', namespace='CELERY')
celery_app.autodiscover_tasks()

celery_app.conf.broker_url = config('CELERY_BROKER_URL')
celery_app.conf.result_backend = config('CELERY_RESULT_BACKEND')
celery_app.conf.task_serializer = 'json'
celery_app.conf.result_serializer = 'json'
celery_app.conf.accept_content = ['json']
celery_app.conf.result_expires = timedelta(days=1)
celery_app.conf.task_always_eager = False
celery_app.conf.worker_prefetch_multiplier = 1

