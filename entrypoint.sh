#!/bin/bash

# Apply database migrations
#python manage.py migrate

# Start the Django server
#python manage.py runserver 0.0.0.0:8000

# Apply database migrations
#django-admin migrate --settings=cows_project.settings
python manage.py migrate --settings=cows_project.settings

# Collect static files
#django-admin collectstatic --noinput --settings=cows_project.settings
python manage.py collectstatic --noinput --settings=cows_project.settings

# Start Gunicorn server
#exec gunicorn cows_project.wsgi:application --bind 0.0.0.0:8000 --workers 3
exec gunicorn cows_project.wsgi:application --bind 0.0.0.0:8000 --workers 1
