docker-compose run app poetry run pytest

# create a distributable package
poetry build 




docker-compose run web poetry run python manage.py makemigrations
docker-compose run web poetry run python manage.py migrate


docker-compose down
docker-compose down -v
