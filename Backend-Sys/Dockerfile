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

RUN pip install django==5.1.2

# Expose the port the app runs on
EXPOSE 8000

# Add wait-for-it script to wait for the database to be ready
COPY runner.sh /runner.sh
RUN chmod +x /runner.sh

# Environment variables for superuser
ENV DJANGO_SUPERUSER_USERNAME=root-admin
ENV DJANGO_SUPERUSER_EMAIL=ai.doesntstop@gmail.com
ENV DJANGO_SUPERUSER_PASSWORD=pass@1234

# Run the application
CMD /wait-for-it.sh $PGHOST:$PGPORT -- venv/bin/python manage.py makemigrations && \
    venv/bin/python manage.py migrate && \
    venv/bin/python manage.py createsuperuser --noinput --username $DJANGO_SUPERUSER_USERNAME --email $DJANGO_SUPERUSER_EMAIL || true && \
    echo "from django.contrib.auth.models import User; user = User.objects.get(username='$DJANGO_SUPERUSER_USERNAME'); user.set_password('$DJANGO_SUPERUSER_PASSWORD'); user.save();" | venv/bin/python manage.py shell && \
    venv/bin/python manage.py runserver 0.0.0.0:8000