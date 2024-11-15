from rest_framework import serializers
from .models import ScheduledReport, DataBreachReport, ComplianceAudit

class ScheduledReportSerializer(serializers.ModelSerializer):
    """Serializer for the ScheduledReport model."""
    
    class Meta:
        model = ScheduledReport
        fields = ['id', 'organization', 'report_type', 'schedule_time', 'interval', 'email_recipients']
        read_only_fields = ['id']

class DataBreachReportSerializer(serializers.ModelSerializer):
    """Serializer for the DataBreachReport model."""
    
    class Meta:
        model = DataBreachReport
        fields = ['id', 'organization', 'incident_date', 'discovery_date', 'description',
                  'affected_data_subjects', 'data_types_affected', 'severity', 'potential_impact',
                  'remediation_steps', 'reported_to_authorities', 'date_reported_to_authorities',
                  'reported_to_data_subjects', 'date_reported_to_data_subjects', 'report_generated_date', 
                  'is_within_72_hours']
        read_only_fields = ['id', 'report_generated_date', 'is_within_72_hours']

class ComplianceAuditSerializer(serializers.ModelSerializer):
    """Serializer for the ComplianceAudit model."""
    
    class Meta:
        model = ComplianceAudit
        fields = ['id', 'organization', 'audit_date', 'auditor', 'audit_findings', 
                  'recommendations', 'is_resolved', 'resolution_date']
        read_only_fields = ['id', 'audit_date']