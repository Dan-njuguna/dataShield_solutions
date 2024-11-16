import sys
sys.dont_write_bytecode = True
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.conf import settings
from .models import User
import logging

logger = logging.getLogger(__name__)

@receiver(post_save, sender=User )
def user_created(sender, instance, created, **kwargs):
    """
    Signal receiver that listens for the post_save signal from the User model.
    
    This function is triggered after a User instance is saved. If the instance
    was newly created, it performs actions such as logging or sending notifications.
    
    Args:
        sender: The model class that sent the signal (User ).
        instance: The actual instance being saved.
        created: Boolean indicating whether a new record was created.
        **kwargs: Additional keyword arguments.
    """
    if created:
        # Log user creation
        logger.info(f"New user created: {instance.email}")
        
        # Send verification email
        token = default_token_generator.make_token(instance)
        verification_link = f"{settings.FRONTEND_URL}/verify-email/?token={token}&email={instance.email}"
        send_mail(
            'Verify your email',
            f'Click this link to verify your email: {verification_link}',
            settings.DEFAULT_FROM_EMAIL,
            [instance.email],
        )
        logger.info(f"Verification email sent to {instance.email}")
    else:
        # Log updates to existing users
        logger.info(f"User  updated: {instance.email}")