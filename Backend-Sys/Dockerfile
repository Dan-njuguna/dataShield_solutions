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
ENV PGHOST=db
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

# Create the staticfiles directory
RUN mkdir -p /app/staticfiles

# Collect the static files
RUN venv/bin/python manage.py collectstatic --noinput

# Making Database Migrations and Static files collection
# Run the migrations
RUN venv/bin/python manage.py makemigrations && venv/bin/python manage.py migrate
# Collect the static files
RUN venv/bin/python manage.py collectstatic --noinput

# Environment variables for superuser
ENV DJANGO_SUPERUSER_USERNAME=root-admin
ENV DJANGO_SUPERUSER_EMAIL=ai.doesntstop@gmail.com
ENV DJANGO_SUPERUSER_PASSWORD=pass@1234

# Create a superuser
# Create superuser and set password
RUN venv/bin/python manage.py createsuperuser --noinput \
    --username $DJANGO_SUPERUSER_USERNAME \
    --email $DJANGO_SUPERUSER_EMAIL || true && \
    echo "from django.contrib.auth.models import User; \
    user = User.objects.get(username='$DJANGO_SUPERUSER_USERNAME'); \
    user.set_password('$DJANGO_SUPERUSER_PASSWORD'); \
    user.save();" | venv/bin/python manage.py shell

# Run the application
ENTRYPOINT ["venv/bin/python", "manage.py", "runserver", "0.0.0.0:8000"]

## Persisting the Database
# The database is stored in a Docker volume, which is a persistent data storage mechanism.
# This allows the database to be stored on the host machine and not be deleted when the container is removed.
