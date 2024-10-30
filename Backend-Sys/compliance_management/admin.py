# decompyle3 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: C:\Users\Susan\OneDrive\Desktop\datashield solutions\Backend-Sys\compliance_management\admin.py
# Compiled at: 2024-10-29 15:14:32
# Size of source mod 2**32: 1649 bytes
from django.contrib import admin
from .models import DataProtectionRegulation, ComplianceStatus, ComplianceReport, ComplianceDocument, DataProcessingActivity, DPIA, Incident

@admin.register(DataProtectionRegulation)
class DataProtectionRegulationAdmin(admin.ModelAdmin):
    list_display = ('name', 'jurisdiction')
    search_fields = ('name', )


@admin.register(ComplianceStatus)
class ComplianceStatusAdmin(admin.ModelAdmin):
    list_display = ('compliance_status', 'organization', 'last_checked_at')
    search_fields = ('organization__name', )


@admin.register(ComplianceReport)
class ComplianceReportAdmin(admin.ModelAdmin):
    list_display = ('organization', 'generated_at', 'report_type')
    search_fields = ('organization__name', 'report_type')


@admin.register(ComplianceDocument)
class ComplianceDocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'organization', 'uploaded_by', 'upload_date')
    search_fields = ('title', 'organization__name')


@admin.register(DataProcessingActivity)
class DataProcessingActivityAdmin(admin.ModelAdmin):
    list_display = ('activity_name', 'organization', 'is_high_risk', 'last_reviewed')
    search_fields = ('activity_name', 'organization__name')


@admin.register(DPIA)
class DPIAAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'organization', 'created_at')
    search_fields = ('project_name', 'organization__name')


@admin.register(Incident)
class IncidentAdmin(admin.ModelAdmin):
    list_display = ('description', 'date', 'reported_by')
    search_fields = ('description', 'reported_by__email')

# okay decompiling admin.cpython-38.pyc
