from django.contrib import admin
from .models import DataProtectionRegulation, ComplianceStatus, ComplianceReport, ComplianceDocument, DataProcessingActivity, DPIA, Incident, KenyaDPA

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

@admin.register(KenyaDPA)  # Registering the KenyaDPA model
class KenyaDPAAdmin(admin.ModelAdmin):
    list_display = ('data_protection_regulation_id', 'category', 'description', 'section_in_act')
    search_fields = ('category', 'description', 'data_protection_regulation_id__name')