#!/bin/bash

python manage.py collectstatic --noinput
python manage.py makemigrations
python manage.py migrate
gunicorn -c gunicorn_config.py cows_project.wsgi:application
