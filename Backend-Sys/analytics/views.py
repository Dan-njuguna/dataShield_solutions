from django.http import JsonResponse
from django.core import serializers
from audit_log.models import AuditLog
from compliance_management.models import ComplianceStatus
from django.utils import timezone
from datetime import timedelta

def metrics_view(request):
    actions_count = AuditLog.objects.filter(created_at__gte=(timezone.now() - timedelta(days=30))).count()
    compliant_count = ComplianceStatus.objects.filter(compliance_status="compliant").count()
    non_compliant_count = ComplianceStatus.objects.filter(compliance_status="non-compliant").count()

    metrics = {
        'actions_count': actions_count,
        'compliant_count': compliant_count,
        'non_compliant_count': non_compliant_count
        }

    return JsonResponse(metrics)



