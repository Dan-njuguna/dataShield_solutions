#!/bin/bash

# Load environment variables from .env file
set -o allexport
source .env
set -o allexport

# Wait for the database to be ready
until docker exec -it $DB_CONTAINER_NAME pg_isready -U $DB_USER -d $DB_NAME; do
    echo "Waiting for database to be ready..."
    sleep 2
done

# Run database migrations
docker exec -it $DB_CONTAINER_NAME psql -U $DB_USER -d $DB_NAME -f /path/to/migrations.sql

echo "Database configured successfully."