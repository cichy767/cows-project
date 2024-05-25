# Użyj obrazu Pythona jako podstawy
FROM python:3.11

# Instalacja Poetry
RUN curl -sSL https://install.python-poetry.org | python3 - && \
    export PATH="/root/.local/bin:$PATH"

# Ustaw katalog roboczy
WORKDIR /app

# Skopiuj pliki konfiguracyjne Poetry
COPY pyproject.toml poetry.lock ./

# Ustawienie ścieżki do Poetry
ENV PATH="/root/.local/bin:$PATH"

# Zainstaluj zależności przy użyciu Poetry
RUN poetry install --no-root

# Skopiuj resztę plików aplikacji
COPY ./source .

# Ustaw zmienną środowiskową dla Flask
ENV FLASK_APP=app.py

# Uruchom aplikację Flask
CMD ["poetry", "run", "flask", "run", "--host=0.0.0.0"]
