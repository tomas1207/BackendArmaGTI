#!/bin/bash
python3 manage.py migrate --no-input
gunicorn Core.wsgi:application --bind 0.0.0.0:4200
