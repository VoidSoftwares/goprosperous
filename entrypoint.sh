#!/bin/sh
echo "Apply Database Migration"
python manage.py migrate --no-input
python manage.py collectstatic --no-input
gunicorn --reload --bind 0.0.0.0:8000 goprosperous.wsgi:application
