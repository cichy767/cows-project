#!/bin/bash

# Apply database migrations
#python manage.py makemigrations
#python manage.py migrate
#python manage.py runserver 0.0.0.0:8000
#poetry run django-admin migrate --settings=cows_project.settings

# Collect static files
#poetry run django-admin collectstatic --noinput --settings=cows_project.settings

# Start Gunicorn server
#exec poetry run gunicorn cows_project.wsgi:application --bind 0.0.0.0:8000 --workers 3



# Apply database migrations
poetry run django-admin migrate --settings=cows_project.cows_project.settings

# Collect static files
#poetry run django-admin collectstatic --noinput --settings=cows_project.settings
#
## Start Gunicorn server with typeguard to enforce type hints
#exec poetry run gunicorn cows_project.wsgi:application --bind 0.0.0.0:8000 --workers 3