# Użyj obrazu Pythona jako podstawy
FROM python:3.11


# Set the working directory in the container
WORKDIR /app

# Install Poetry
RUN pip install poetry gunicorn

# Copy pyproject.toml and poetry.lock files to the container
COPY pyproject.toml poetry.lock ./

# Install the dependencies
RUN poetry install --no-dev

# Copy the package tarball and install it
COPY dist/cows_project-0.1.0.tar.gz ./
#RUN poetry add nn-0.1.0.tar.gz
# Install the packaged project
RUN poetry run pip install ./cows_project-0.1.0.tar.gz

#RUN pip install nn-0.1.0.tar.gz

# Copy the rest of the application code
COPY . .

# Copy entrypoint script
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Define the entrypoint
ENTRYPOINT ["/entrypoint.sh"]