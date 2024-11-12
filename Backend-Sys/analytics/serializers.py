from rest_framework import serializers

class MetricsSerializer(serializers.Serializer):
    """Serializer for metrics data."""
    actions_count = serializers.IntegerField()
    compliant_count = serializers.IntegerField()
    non_compliant_count = serializers.IntegerField()