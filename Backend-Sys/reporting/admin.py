# decompyle3 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: C:\Users\Susan\OneDrive\Desktop\datashield solutions\Backend-Sys\reporting\admin.py
# Compiled at: 2024-10-29 15:34:08
# Size of source mod 2**32: 779 bytes
from django.contrib import admin
from .models import ScheduledReport, DataBreachReport, ComplianceAudit

@admin.register(ScheduledReport)
class ScheduledReportAdmin(admin.ModelAdmin):
    list_display = ('organization', 'report_type', 'schedule_time', 'interval')
    search_fields = ('organization__name', 'report_type')


@admin.register(DataBreachReport)
class DataBreachReportAdmin(admin.ModelAdmin):
    list_display = ('organization', 'incident_date', 'discovery_date', 'severity')
    search_fields = ('organization__name', 'description')


@admin.register(ComplianceAudit)
class ComplianceAuditAdmin(admin.ModelAdmin):
    list_display = ('organization', 'audit_date', 'auditor', 'is_resolved')
    search_fields = ('organization__name', 'audit_findings')

# okay decompiling admin.cpython-38.pyc
