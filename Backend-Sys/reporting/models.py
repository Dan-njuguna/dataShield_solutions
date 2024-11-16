import sys
sys.dont_write_bytecode = True
from django.db import models
from authentication.models import Organization, User
from django.utils import timezone
from django.core.exceptions import ValidationError

from dotenv import load_dotenv
import os
load_dotenv()

class ScheduledReport(models.Model):
    __doc__ = "Model representing a scheduled compliance report for an organization."
    organization = models.ForeignKey(Organization, on_delete=(models.CASCADE), help_text="The organization for which the report is scheduled.")
    report_type = models.CharField(max_length=100, help_text="Type of the scheduled report.")
    schedule_time = models.DateTimeField(help_text="The time when the report is scheduled to be generated.")
    interval = models.CharField(max_length=50, help_text="Interval for report generation (e.g., daily, weekly, monthly).")
    email_recipients = models.TextField(help_text="Comma-separated email addresses of recipients for the report.")

    def __str__(self):
        """Return string representation of the scheduled report."""
        return f"Scheduled {self.report_type} for {self.organization} at {self.schedule_time}"


class DataBreachReport(models.Model):
    __doc__ = "Model representing a report of a data breach incident."
    SEVERITY_CHOICES = [
     ('LOW', 'Low'),
     ('MEDIUM', 'Medium'),
     ('HIGH', 'High'),
     ('CRITICAL', 'Critical')]
    organization = models.ForeignKey(Organization, on_delete=(models.CASCADE), help_text="The organization affected by the data breach.")
    incident_date = models.DateTimeField(help_text="Date and time when the incident occurred.")
    discovery_date = models.DateTimeField(help_text="Date and time when the incident was discovered.")
    description = models.TextField(help_text="Description of the data breach incident.")
    affected_data_subjects = models.IntegerField(help_text="Number of data subjects affected by the breach.")
    data_types_affected = models.TextField(help_text="Types of data that were affected in the breach.")
    severity = models.CharField(max_length=10, choices=SEVERITY_CHOICES, help_text="Severity level of the data breach.")
    potential_impact = models.TextField(help_text="Potential impact of the data breach.")
    remediation_steps = models.TextField(help_text="Steps taken to remediate the breach.")
    reported_to_authorities = models.BooleanField(default=False, help_text="Indicates if the breach was reported to authorities.")
    date_reported_to_authorities = models.DateTimeField(null=True, blank=True, help_text="Date when the breach was reported to authorities.")
    reported_to_data_subjects = models.BooleanField(default=False, help_text="Indicates if the breach was reported to affected data subjects.")
    date_reported_to_data_subjects = models.DateTimeField(null=True, blank=True, help_text="Date when the breach was reported to data subjects.")
    report_generated_date = models.DateTimeField(auto_now_add=True, help_text="Timestamp when the breach report was generated.")
    is_within_72_hours = models.BooleanField(help_text="Indicates if the breach was reported within 72 hours of discovery.")

    def clean(self):
        """Validate the data breach report before saving."""
        if self.discovery_date > timezone.now():
            raise ValidationError("Discovery date cannot be in the future.")

    def save(self, *args, **kwargs):
        """Override save method to perform validation and set is_within_72_hours."""
        self.clean()
        if not self.pk:
            self.is_within_72_hours = timezone.now() - self.discovery_date <= timezone.timedelta(hours=72)
        (super().save)(*args, **kwargs)

    def __str__(self):
        """Return string representation of the data breach report."""
        return f'Data Breach Report for {self.organization} on {self.incident_date.strftime("%Y-%m-%d")}'


class ComplianceAudit(models.Model):
    __doc__ = "Model representing a compliance audit conducted for an organization."
    organization = models.ForeignKey(Organization, on_delete=(models.CASCADE), help_text="The organization that is being audited.")
    audit_date = models.DateTimeField(auto_now_add=True, help_text="Date when the audit was conducted.")
    auditor = models.ForeignKey(User, on_delete=(models.SET_NULL), null=True, help_text="The user who conducted the audit.")
    audit_findings = models.TextField(help_text="Findings from the audit.")
    recommendations = models.TextField(help_text="Recommendations based on the audit findings.")
    is_resolved = models.BooleanField(default=False, help_text="Indicates if the findings have been resolved.")
    resolution_date = models.DateTimeField(null=True, blank=True, help_text="Date when the findings were resolved.")

    def __str__(self):
        """Return string representation of the compliance audit."""
        return f'Compliance Audit for {self.organization} on {self.audit_date.strftime("%Y-%m-%d")}'
