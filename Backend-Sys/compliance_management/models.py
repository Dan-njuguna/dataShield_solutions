from django.db import models
from authentication.models import Organization, User
from dotenv import load_dotenv
import os


class DataProtectionRegulation(models.Model):
    """Model representing a data protection regulation."""
    name = models.CharField(max_length=255, help_text="Name of the data protection regulation.")
    jurisdiction = models.CharField(max_length=100, blank=True, help_text="Jurisdiction of the regulation.")
    description = models.TextField(blank=True, help_text="Description of the regulation.")

    def __str__(self):
        """Return string representation of the regulation."""
        return self.name


class KenyaDPA(models.Model):
    """Model representing the data protection regulations specific to Kenya."""
    id = models.AutoField(primary_key=True)  # Explicitly defining the id field
    data_protection_regulation_id = models.ForeignKey(
        DataProtectionRegulation,
        on_delete=models.CASCADE,
        help_text="The associated data protection regulation."
    )
    category = models.CharField(max_length=255, help_text="Category of the data protection requirement.")
    description = models.TextField(help_text="Description of the requirement.")
    section_in_act = models.CharField(max_length=255, help_text="Section in the act related to the requirement.")
    key_points = models.TextField(help_text="Key points related to the requirement.")

    def __str__(self):
        """Return string representation of the Kenya DPA entry."""
        return f"{self.category}: {self.description[:50]}..." 

class ComplianceStatus(models.Model):
    """Model representing the compliance status of an organization."""
    COMPLIANCE_STATUS_CHOICES = [
        ('compliant', 'Compliant'),
        ('non-compliant', 'Non-Compliant')
    ]
    compliance_status = models.CharField(max_length=20, choices=COMPLIANCE_STATUS_CHOICES, help_text="The compliance status of the organization.")
    last_checked_at = models.DateTimeField(auto_now=True, help_text="Timestamp of the last compliance check.")
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, help_text="The organization for which the compliance status is recorded.")
    data_protection_regulations = models.ForeignKey(DataProtectionRegulation, on_delete=models.SET_NULL, null=True, blank=True, help_text="Related data protection regulations.")

    def __str__(self):
        """Return string representation of the compliance status."""
        return f'{self.compliance_status} for {self.organization.name} on {self.last_checked_at.strftime("%Y-%m-%d")}'


class ComplianceReport(models.Model):
    """Model representing a compliance report generated for an organization."""
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, help_text="The organization for which the report is generated.")
    generated_at = models.DateTimeField(auto_now_add=True, help_text="Timestamp of when the report was generated.")
    report_type = models.CharField(max_length=100, help_text="Type of the compliance report.")
    filters = models.JSONField(help_text="Filters used during report generation.")
    file = models.FileField(upload_to="compliance_reports/", help_text="The generated report file.")

    class Meta:
        indexes = [
            models.Index(fields=["organization", "generated_at"]),
            models.Index(fields=["report_type"])
        ]

    def __str__(self):
        """Return string representation of the compliance report."""
        return f"Report for {self.organization} on {self.generated_at}"


class ComplianceDocument(models.Model):
    """Model representing a compliance document uploaded by an organization."""
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, help_text="The organization that uploaded the document.")
    title = models.CharField(max_length=255, help_text="Title of the compliance document.")
    document_type = models.CharField(max_length=100, help_text="Type of the compliance document.")
    file = models.FileField(upload_to="compliance_documents/", help_text="The uploaded compliance document file.")
    uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, help_text="The user who uploaded the document.")
    upload_date = models.DateTimeField(auto_now_add=True, help_text="Timestamp when the document was uploaded.")
    expiry_date = models.DateField(null=True, blank=True, help_text="Expiry date of the compliance document.")

    def __str__(self):
        """Return string representation of the compliance document."""
        return self.title


class DataProcessingActivity(models.Model):
    """Model representing a data processing activity conducted by an organization."""
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, help_text="The organization conducting the data processing activity.")
    activity_name = models.CharField(max_length=255, help_text="Name of the data processing activity.")
    purpose = models.TextField(help_text="Purpose of the data processing activity.")
    data_categories = models.TextField(help_text="Categories of data being processed.")
    data_subjects = models.TextField(help_text="Data subjects whose data is being processed.")
    retention_period = models.CharField(max_length=100, help_text="Duration for which the data will be retained.")
    security_measures = models.TextField(help_text="Security measures in place for the data processing activity.")
    is_high_risk = models.BooleanField(default=False, help_text="Indicates if the processing activity is considered high risk.")
    last_reviewed = models.DateField(auto_now=True, help_text="Date when the data processing activity was last reviewed.")

    def __str__(self):
        """Return string representation of the data processing activity."""
        return f"{self.activity_name} - {self.organization}"


class DPIA(models.Model):
    """Model representing a Data Protection Impact Assessment (DPIA)."""
    project_name = models.CharField(max_length=255)
    description = models.TextField()
    data_types = models.JSONField()
    risks = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, help_text="The organization for which the DPIA is conducted.")

    def __str__(self):
        """Return a string representation of the DPIA."""
        return self.project_name


class Incident(models.Model):
    """Model representing an incident report."""
    description = models.TextField()
    date = models.DateField(auto_now_add=True)
    reported_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, help_text="The user who reported the incident.")

    def __str__(self):
        """Return a string representation of the incident."""
        return self.description