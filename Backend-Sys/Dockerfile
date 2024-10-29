FROM python:3.12.3-slim

# Set the working directory
WORKDIR /app

# Update pip to the latest version and install system dependencies
RUN apt-get update && apt-get install -y \
    libpq-dev \
    build-essential \
    gcc \
    postgresql-client \
    && pip install --upgrade pip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Increase pip timeout
ENV PIP_DEFAULT_TIMEOUT=100

# Configure the environment for PostgreSQL
ENV PGHOST=postgres
ENV PGPORT=5432
ENV PGUSER=data_shield
ENV PGPASSWORD=data_shield_pass
ENV PGDATABASE=data_shield_db

# Copy the requirements file and install dependencies
COPY ../requirements.txt /app/requirements.txt

# Install virtualenv and create a virtual environment
RUN pip install virtualenv \
    && virtualenv venv \
    && . venv/bin/activate \
    && pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . /app

# Expose the port the app runs on
EXPOSE 8000

# Run the application
ENTRYPOINT ["venv/bin/python", "manage.py", "runserver", "0.0.0.0:8000"]

## Persisting the Database
# The database is stored in a Docker volume, which is a persistent data storage mechanism.
# This allows the database to be stored on the host machine and not be deleted when the container is removed.
