import sys
sys.dont_write_bytecode = True
from rest_framework import serializers
from .models import DataProtectionRegulation, ComplianceStatus, ComplianceReport, ComplianceDocument, DataProcessingActivity, DPIA, Incident, KenyaDPA

class DataProtectionRegulationSerializer(serializers.ModelSerializer):
    """Serializer for DataProtectionRegulation model."""
    class Meta:
        model = DataProtectionRegulation
        fields = ['id', 'name', 'jurisdiction', 'description']


class KenyaDPASerializer(serializers.ModelSerializer):
    """Serializer for KenyaDPA model."""
    class Meta:
        model = KenyaDPA
        fields = '__all__'

class ComplianceStatusSerializer(serializers.ModelSerializer):
    """Serializer for ComplianceStatus model."""
    class Meta:
        model = ComplianceStatus
        fields = ['id', 'compliance_status', 'organization', 'data_protection_regulations', 'last_checked_at']

class ComplianceReportSerializer(serializers.ModelSerializer):
    """Serializer for ComplianceReport model."""
    class Meta:
        model = ComplianceReport
        fields = ['id', 'organization', 'generated_at', 'report_type', 'filters', 'file']

class ComplianceDocumentSerializer(serializers.ModelSerializer):
    """Serializer for ComplianceDocument model."""
    class Meta:
        model = ComplianceDocument
        fields = ['id', 'organization', 'title', 'document_type', 'file', 'uploaded_by', 'upload_date', 'expiry_date']

class DataProcessingActivitySerializer(serializers.ModelSerializer):
    """Serializer for DataProcessingActivity model."""
    class Meta:
        model = DataProcessingActivity
        fields = ['id', 'organization', 'activity_name', 'purpose', 'data_categories', 'data_subjects', 'retention_period', 'security_measures', 'is_high_risk', 'last_reviewed']

class DPIASerializer(serializers.ModelSerializer):
    """Serializer for DPIA model."""
    class Meta:
        model = DPIA
        fields = ['id', 'project_name', 'description', 'data_types', 'risks', 'created_at', 'organization']

class IncidentSerializer(serializers.ModelSerializer):
    """Serializer for Incident model."""
    class Meta:
        model = Incident
        fields = ['id', 'description', 'date', 'reported_by']