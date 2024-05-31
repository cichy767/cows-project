FROM python:3.11-slim

ENV USER=appuser
ENV USERGROUP=bootgrp
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    curl \
    && apt-get clean


# Copy the .whl file into the container
COPY dist/cows_project-0.1.0-py3-none-any.whl /app/

# Install the .whl package
RUN pip install /app/cows_project-0.1.0-py3-none-any.whl
# Expose the port the app runs on
EXPOSE 8000
RUN groupadd -r -g 999 $USERGROUP && useradd -m -u 999 -g $USERGROUP $USER

RUN mkdir -p /var/www/static/
RUN chown -R $USER:$USERGROUP \
    /var/www/static \
    /app

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
# Switch to non-root user
USER $USER

ENTRYPOINT ["/entrypoint.sh"]
