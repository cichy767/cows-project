FROM python:3.11-slim-buster

RUN apt-get update && apt-get upgrade -y
RUN pip install poetry gunicorn

ENV APP_ROOT /app
WORKDIR ${APP_ROOT}

ARG POETRY_VERSION=1.4.2
RUN pip install poetry==$POETRY_VERSION
RUN poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock ./
RUN poetry install --no-dev

COPY . ${APP_ROOT}

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh


# Set environment variables
ENV PYTHONUNBUFFERED 1

# Define the entrypoint
ENTRYPOINT ["/entrypoint.sh"]
#CMD ["gunicorn", "-c", "gunicorn_config.py", "config.wsgi:application"]
