FROM python:3.11

WORKDIR /app

COPY ../cows_project/pyproject.toml ./
COPY ../cows_project/poetry.lock ./


RUN pip install poetry && poetry install

COPY .. .
WORKDIR /app/cows_project

CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]

