from django.contrib import admin
from .models import Organization, User, DataProtectionRegulation, Gdpr4, KenyaDPA, ComplianceStatus, ComplianceStatusTracking

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'contact_person', 'contact_email','contact_number', 'industry', 'company_size', 'created_at')
    search_fields = ('name','industry', 'contact_person', 'contact_email')

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'first_name', 'last_name', 'organization', 'is_staff', 'is_active')
    search_fields = ('email', 'first_name', 'last_name', 'organization')

@admin.register(DataProtectionRegulation)
class DataProtectionRegulationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'jurisdiction', 'description')
    search_fields = ('name',)

@admin.register(Gdpr4)
class Gdpr4Admin(admin.ModelAdmin):
    list_display = ('id', 'category', 'description', 'data_protection_regulation')
    search_fields = ('category',)

@admin.register(KenyaDPA)
class KenyaDPAAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'section_in_act', 'data_protection_regulation')
    search_fields = ('category',)

@admin.register(ComplianceStatus)
class ComplianceStatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'compliance_status', 'last_checked_at', 'organization')
    search_fields = ('compliance_status',)

@admin.register(ComplianceStatusTracking)
class ComplianceStatusTrackingAdmin(admin.ModelAdmin):
    list_display = ('id', 'compliance_status', 'new_compliance_status', 'changed_at')
    search_fields = ('new_compliance_status',)