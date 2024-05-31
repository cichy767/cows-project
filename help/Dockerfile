# Użyj obrazu Pythona jako podstawy
FROM python:3.11

WORKDIR /app

COPY ../pyproject.toml poetry.lock ./
RUN pip install poetry && poetry install

COPY .. .
WORKDIR /app/cows_project

CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]

