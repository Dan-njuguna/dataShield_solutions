# analytics/tasks.py
from celery import shared_task
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.utils import timezone
from datetime import timedelta
from audit_log.models import AuditLog
from compliance_management.models import ComplianceStatus

@shared_task
def broadcast_metrics():
    """
    Broadcast metrics data to WebSocket clients.
    This task retrieves metrics and sends them to the metrics group.
    """
    channel_layer = get_channel_layer()
    
    # Calculate metrics
    actions_count = AuditLog.objects.filter(created_at__gte=timezone.now() - timedelta(days=30)).count()
    compliant_count = ComplianceStatus.objects.filter(compliance_status='compliant').count()
    non_compliant_count = ComplianceStatus.objects.filter(compliance_status='non-compliant').count()

    metrics = {
        'actions_count': actions_count,
        'compliant_count': compliant_count,
        'non_compliant_count': non_compliant_count,
    }

    # Send metrics to the metrics group
    async_to_sync(channel_layer.group_send)(
        "metrics_group",
        {
            'type': 'send_metrics',
            'metrics': metrics
        }
    )