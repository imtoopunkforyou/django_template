import os

from celery import Celery


launch_point = os.environ.get('LAUNCH_POINT', 'local')
if launch_point == 'stand':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.stand')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.local')

app = Celery("core")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
