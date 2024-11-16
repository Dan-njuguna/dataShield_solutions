import sys
sys.dont_write_bytecode = True
from django.apps import AppConfig


class ReportingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'reporting'
