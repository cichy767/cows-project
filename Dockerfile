# Use an official Python runtime as a parent image
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Install Poetry and Gunicorn
RUN pip install poetry gunicorn

# Copy pyproject.toml and poetry.lock files to the container
COPY pyproject.toml poetry.lock ./

# Install the dependencies
RUN poetry install --no-dev

# Copy the rest of the application code
COPY . .

# Copy entrypoint script
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Define the entrypoint
ENTRYPOINT ["/entrypoint.sh"]
