from django.contrib import admin
from .models import User, Organization

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'organization', 'is_active',
                    'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    prepopulated_fields = {"slug": ('email', )}


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_person', 'contact_email', 'industry', 'company_size')
    search_fields = ('name', 'contact_person', 'industry')
    prepopulated_fields = {"slug": ('name', )}
