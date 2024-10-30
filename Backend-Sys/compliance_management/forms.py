# decompyle3 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: C:\Users\Susan\OneDrive\Desktop\datashield solutions\Backend-Sys\compliance_management\forms.py
# Compiled at: 2024-10-29 15:14:07
# Size of source mod 2**32: 1548 bytes
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

# okay decompiling forms.cpython-38.pyc
