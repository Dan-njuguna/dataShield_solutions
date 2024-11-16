import sys
sys.dont_write_bytecode = True
from rest_framework import serializers
from .models import Policy, PolicyVersion, ApprovalWorkflow

class PolicySerializer(serializers.ModelSerializer):
    """Serializer for the Policy model."""
    
    class Meta:
        model = Policy
        fields = ['id', 'title', 'slug', 'description', 'created_at', 'updated_at', 'created_by', 'is_active']
        read_only_fields = ['created_at', 'updated_at', 'created_by']

class PolicyVersionSerializer(serializers.ModelSerializer):
    """Serializer for the PolicyVersion model."""
    
    class Meta:
        model = PolicyVersion
        fields = ['id', 'policy', 'version_number', 'document', 'created_at', 'created_by']
        read_only_fields = ['created_at', 'created_by']

class ApprovalWorkflowSerializer(serializers.ModelSerializer):
    """Serializer for the ApprovalWorkflow model."""
    
    class Meta:
        model = ApprovalWorkflow
        fields = ['id', 'policy', 'approved_by', 'approved_at', 'status']
        read_only_fields = ['approved_at']