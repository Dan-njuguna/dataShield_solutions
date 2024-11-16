import sys
sys.dont_write_bytecode = True
from django.apps import AppConfig

class ComplianceManagementConfig(AppConfig):
    """Configuration class for the Compliance Management app."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'compliance_management'