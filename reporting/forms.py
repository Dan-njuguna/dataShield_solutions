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

