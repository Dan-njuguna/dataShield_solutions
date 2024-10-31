from django.db import models
from authentication.models import Organization, User

from decouple import config

DBUSER = config('DBUSER')
DBNAME = config("DBNAME")
DBPASS = config("DBPASS")
DBHOST = config("DBHOST")
DBPORT = config("DBPORT")

class AuditLog(models.Model):
    __doc__ = "Model representing an audit log entry for actions performed in the system."
    ACTION_CHOICES = [
     ('CREATE', 'Create'),
     ('READ', 'Read'),
     ('UPDATE', 'Update'),
     ('DELETE', 'Delete'),
     ('LOGIN', 'Login'),
     ('LOGOUT', 'Logout'),
     ('EXPORT', 'Export Data'),
     ('IMPORT', 'Import Data'),
     ('COMPLIANCE_CHECK', 'Compliance Check')]
    organization = models.ForeignKey(Organization, on_delete=(models.CASCADE), help_text="The organization related to the action.")
    user = models.ForeignKey(User, on_delete=(models.SET_NULL), null=True, blank=True, help_text="The user who performed the action.")
    action = models.CharField(max_length=20, choices=ACTION_CHOICES, help_text="The action performed.")
    action_description = models.TextField(help_text="Description of the action performed.")
    affected_resource = models.CharField(max_length=100, help_text="The resource affected by the action.")
    ip_address = models.GenericIPAddressField(null=True, blank=True, help_text="IP address from which the action was performed.")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Timestamp when the action was logged.")
    is_compliant = models.BooleanField(default=True, help_text="Indicates if the action was compliant.")
    compliance_notes = models.TextField(blank=True, help_text="Notes regarding compliance.")
    additional_data = models.JSONField(null=True, blank=True, help_text="Store additional data as JSON.")

    def __str__(self):
        """Return string representation of the audit log entry."""
        return f'{self.action} on {self.affected_resource} by {self.user or "System"} at {self.created_at}'

    @classmethod
    def log_action(cls, organization, user, action, description, resource, ip_address=None, is_compliant=True, compliance_notes=''):
        """
        Log an action performed in the system.
        
        Args:
            organization (Organization): The organization related to the action.
            user (User ): The user who performed the action.
            action (str): The action performed.
            description (str): Description of the action.
            resource (str): The resource affected by the action.
            ip_address (str, optional): IP address from which the action was performed. Defaults to None.
            is_compliant (bool, optional): Indicates if the action was compliant. Defaults to True.
            compliance_notes (str, optional): Notes regarding compliance. Defaults to an empty string.
        
        Returns:
            AuditLog: The created audit log entry.
        """
        return cls.objects.create(organization=organization,
          user=user,
          action=action,
          action_description=description,
          affected_resource=resource,
          ip_address=ip_address,
          is_compliant=is_compliant,
          compliance_notes=compliance_notes)

    class Meta:
        ordering = [
         "-created_at"]
        indexes = [
         models.Index(fields=["organization", "created_at"]),
         models.Index(fields=["action", "created_at"])]


