#!/bin/sh
python manage.py migrate
python manage.py collectstatic --no-input
uwsgi --ini core/uwsgi.ini