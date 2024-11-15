from django.contrib import admin
from .models import DataProtectionRegulation, ComplianceStatus, ComplianceReport, ComplianceDocument, DataProcessingActivity, DPIA, Incident, KenyaDPA

@admin.register(DataProtectionRegulation)
class DataProtectionRegulationAdmin(admin.ModelAdmin):
    """Admin interface for managing data protection regulations."""
    list_display = ('name', 'jurisdiction')
    search_fields = ('name',)


@admin.register(ComplianceStatus)
class ComplianceStatusAdmin(admin.ModelAdmin):
    """Admin interface for managing compliance statuses."""
    list_display = ('compliance_status', 'organization', 'last_checked_at')
    search_fields = ('organization__name',)


@admin.register(ComplianceReport)
class ComplianceReportAdmin(admin.ModelAdmin):
    """Admin interface for managing compliance reports."""
    list_display = ('organization', 'generated_at', 'report_type')
    search_fields = ('organization__name', 'report_type')


@admin.register(ComplianceDocument)
class ComplianceDocumentAdmin(admin.ModelAdmin):
    """Admin interface for managing compliance documents."""
    list_display = ('title', 'organization', 'uploaded_by', 'upload_date')
    search_fields = ('title', 'organization__name')


@admin.register(DataProcessingActivity)
class DataProcessingActivityAdmin(admin.ModelAdmin):
    """Admin interface for managing data processing activities."""
    list_display = ('activity_name', 'organization', 'is_high_risk', 'last_reviewed')
    search_fields = ('activity_name', 'organization__name')


@admin.register(DPIA)
class DPIAAdmin(admin.ModelAdmin):
    """Admin interface for managing Data Protection Impact Assessments (DPIAs)."""
    list_display = ('project_name', 'organization', 'created_at')
    search_fields = ('project_name', 'organization__name')


@admin.register(Incident)
class IncidentAdmin(admin.ModelAdmin):
    """Admin interface for managing incident reports."""
    list_display = ('description', 'date', 'reported_by')
    search_fields = ('description', 'reported_by__email')


@admin.register(KenyaDPA)
class KenyaDPAAdmin(admin.ModelAdmin):
    """Admin interface for managing Kenya DPA entries."""
    list_display = ('data_protection_regulation_id', 'category', 'description', 'section_in_act')
    search_fields = ('category', 'description', 'data_protection_regulation__name')