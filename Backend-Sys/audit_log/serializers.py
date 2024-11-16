import sys
sys.dont_write_bytecode = True
from rest_framework import serializers
from .models import AuditLog

class AuditLogSerializer(serializers.ModelSerializer):
    """Serializer for the AuditLog model."""
    
    class Meta:
        model = AuditLog
        fields = ['id', 'organization', 'user', 'action', 'action_description',
                  'affected_resource', 'ip_address', 'is_compliant', 
                  'compliance_notes', 'additional_data', 'created_at']
        read_only_fields = ['id', 'created_at', 'user']  