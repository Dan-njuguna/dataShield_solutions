import sys
sys.dont_write_bytecode = True
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import AnonRateThrottle
from audit_log.models import AuditLog
from compliance_management.models import ComplianceStatus
from .serializers import MetricsSerializer
from django.utils import timezone
from datetime import timedelta
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

class MetricsView(APIView):
    """
    API view to retrieve metrics data including actions count and compliance status.
    
    This view provides aggregated metrics for actions performed and compliance status
    over the last 30 days.
    """
    permission_classes = [IsAuthenticated]  # Require authentication
    throttle_classes = [AnonRateThrottle]   # Throttle for anonymous users

    def get(self, request):
        """Handle GET request to retrieve metrics."""
        actions_count = AuditLog.objects.filter(created_at__gte=(timezone.now() - timedelta(days=30))).count()
        compliant_count = ComplianceStatus.objects.filter(compliance_status="compliant").count()
        non_compliant_count = ComplianceStatus.objects.filter(compliance_status="non-compliant").count()

        metrics = {
            'actions_count': actions_count,
            'compliant_count': compliant_count,
            'non_compliant_count': non_compliant_count
        }

        serializer = MetricsSerializer(metrics)

        # Broadcast metrics to WebSocket clients
        self.broadcast_metrics(metrics)

        return Response(serializer.data)

    def broadcast_metrics(self, metrics):
        """Broadcast metrics to WebSocket clients."""
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "metrics_group",
            {
                "type": "send_metrics",
                "metrics": metrics,
            }
        )