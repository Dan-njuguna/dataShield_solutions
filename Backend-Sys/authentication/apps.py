from django.apps import AppConfig

class AuthenticationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'authentication'
    verbose_name = 'User  Authentication'  # A human-readable name for the app

    def ready(self):
        # Import signals to ensure they are registered
        import authentication.signals  # Adjust the import path if necessary