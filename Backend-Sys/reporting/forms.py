# decompyle3 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: C:\Users\Susan\OneDrive\Desktop\datashield solutions\Backend-Sys\reporting\forms.py
# Compiled at: 2024-10-29 15:34:25
# Size of source mod 2**32: 971 bytes
from django import forms
from .models import ScheduledReport, DataBreachReport, ComplianceAudit

class ScheduledReportForm(forms.ModelForm):

    class Meta:
        model = ScheduledReport
        fields = ('organization', 'report_type', 'schedule_time', 'interval', 'email_recipients')


class DataBreachReportForm(forms.ModelForm):

    class Meta:
        model = DataBreachReport
        fields = ('organization', 'incident_date', 'discovery_date', 'description',
                  'affected_data_subjects', 'data_types_affected', 'severity', 'potential_impact',
                  'remediation_steps', 'reported_to_authorities', 'date_reported_to_authorities',
                  'reported_to_data_subjects', 'date_reported_to_data_subjects')


class ComplianceAuditForm(forms.ModelForm):

    class Meta:
        model = ComplianceAudit
        fields = ('organization', 'auditor', 'audit_findings', 'recommendations', 'is_resolved',
                  'resolution_date')

# okay decompiling forms.cpython-38.pyc
