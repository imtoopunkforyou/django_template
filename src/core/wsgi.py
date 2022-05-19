"""
WSGI config for core project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

launch_point = os.environ.get('LAUNCH_POINT', 'local')
if launch_point == 'stand':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.stand')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.local')

application = get_wsgi_application()
