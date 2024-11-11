from django import forms
from .models import DataProtectionRegulation, ComplianceStatus, ComplianceReport, ComplianceDocument, DataProcessingActivity, DPIA, Incident

class DataProtectionRegulationForm(forms.ModelForm):

    class Meta:
        model = DataProtectionRegulation
        fields = ["name", "jurisdiction", "description"]


class ComplianceStatusForm(forms.ModelForm):

    class Meta:
        model = ComplianceStatus
        fields = ["compliance_status", "organization", "data_protection_regulations"]


class ComplianceReportForm(forms.ModelForm):

    class Meta:
        model = ComplianceReport
        fields = ["organization", "report_type", "filters", "file"]


class ComplianceDocumentForm(forms.ModelForm):

    class Meta:
        model = ComplianceDocument
        fields = ["organization","title","document_type","file","uploaded_by","expiry_date"]


class DataProcessingActivityForm(forms.ModelForm):

    class Meta:
        model = DataProcessingActivity
        fields = [
         "organization", "activity_name", "purpose", "data_categories",
         "data_subjects", "retention_period", "security_measures", "is_high_risk"]


class DPIAForm(forms.ModelForm):

    class Meta:
        model = DPIA
        fields = ["project_name","description","data_types","risks","organization"]


class IncidentForm(forms.ModelForm):

    class Meta:
        model = Incident
        fields = ["description", "reported_by"]

