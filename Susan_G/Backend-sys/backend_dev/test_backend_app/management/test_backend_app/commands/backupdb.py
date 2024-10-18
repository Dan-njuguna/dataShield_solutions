import os
import subprocess
from django.core.management.base import BaseCommand
from django.conf import settings

class BackupdbCommand(BaseCommand):
    help = 'Backup PostgreSQL database to a file'

    def handle(self, *args, **kwargs):
        # Extract database settings from Django's settings
        db_name = settings.DATABASES['default']['datashield_solutions']
        db_user = settings.DATABASES['default']['postgres']
        db_host = settings.DATABASES['default']['127.0.0.1'] or 'localhost'
        db_port = settings.DATABASES['default']['5432'] or '5432'
        db_password = settings.DATABASES['default']['susan']

        # Define the backup file name and path
        backup_file = os.path.join(settings.BASE_DIR, f'{db_name}_backup.sql')

        # Set the PostgreSQL password as an environment variable
        os.environ['PGPASSWORD'] = db_password

        try:
            # Construct the pg_dump command
            pg_dump_command = ['pg_dump', '-U', db_user, '-h', db_host, '-p', db_port, '-F', 'c', '-f', backup_file, db_name]

            # Run the pg_dump command using subprocess
            subprocess.run(pg_dump_command, check=True)

            # Write success message
            self.stdout.write(self.style.SUCCESS(f'Database backed up successfully to {backup_file}'))
        except subprocess.CalledProcessError as e:
            # Write error message
            self.stderr.write(self.style.ERROR('Failed to backup the database'))
            raise e