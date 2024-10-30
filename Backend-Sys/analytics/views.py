# decompyle3 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: C:\Users\Susan\OneDrive\Desktop\datashield solutions\Backend-Sys\analytics\views.py
# Compiled at: 2024-10-29 16:03:05
# Size of source mod 2**32: 904 bytes
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
    metrics = {'actions_count':actions_count, 
     'compliant_count':compliant_count, 
     'non_compliant_count':non_compliant_count}
    return JsonResponse(metrics)

# okay decompiling views.cpython-38.pyc
