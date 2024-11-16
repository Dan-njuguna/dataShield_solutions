import sys
sys.dont_write_bytecode = True
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

