#!/bin/sh

python3 manage.py migrate --no-input
gunicorn --bind 0.0.0.0:4200 --timeout 30 --workers 5 --log-level debug Core.wsgi:application