import sys
sys.dont_write_bytecode = True
from django import forms
from .models import DataProtectionRegulation, ComplianceStatus, ComplianceReport, ComplianceDocument, DataProcessingActivity, DPIA, Incident

class DataProtectionRegulationForm(forms.ModelForm):
    """Form for creating and updating data protection regulations."""
    class Meta:
        model = DataProtectionRegulation
        fields = ["name", "jurisdiction", "description"]


class ComplianceStatusForm(forms.ModelForm):
    """Form for creating and updating compliance statuses."""
    class Meta:
        model = ComplianceStatus
        fields = ["compliance_status", "organization", "data_protection_regulations"]


class ComplianceReportForm(forms.ModelForm):
    """Form for creating and updating compliance reports."""
    class Meta:
        model = ComplianceReport
        fields = ["organization", "report_type", "filters", "file"]


class ComplianceDocumentForm(forms.ModelForm):
    """Form for creating and updating compliance documents."""
    class Meta:
        model = ComplianceDocument
        fields = ["organization", "title", "document_type", "file", "uploaded_by", "expiry_date"]


class DataProcessingActivityForm(forms.ModelForm):
    """Form for creating and updating data processing activities."""
    class Meta:
        model = DataProcessingActivity
        fields = [
            "organization", "activity_name", "purpose", "data_categories",
            "data_subjects", "retention_period", "security_measures", "is_high_risk"
        ]


class DPIAForm(forms.ModelForm):
    """Form for creating and updating Data Protection Impact Assessments (DPIAs)."""
    class Meta:
        model = DPIA
        fields = ["project_name", "description", "data_types", "risks", "organization"]


class IncidentForm(forms.ModelForm):
    """Form for creating and updating incident reports."""
    class Meta:
        model = Incident
        fields = ["description", "reported_by"]