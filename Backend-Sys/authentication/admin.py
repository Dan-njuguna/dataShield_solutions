from django.contrib import admin
from .models import User, Organization

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'organization', 'is_active', 'is_staff', 'created_at')
    search_fields = ('email', 'first_name', 'last_name')
    list_filter = ('is_active', 'is_staff', 'organization')
    ordering = ('last_name', 'first_name')
    prepopulated_fields = {"slug": ('email', )}
    date_hierarchy = 'created_at'  # Allows for date-based navigation

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.select_related('organization')  # Optimize queries with select_related


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_person', 'contact_email', 'industry', 'company_size', 'created_at')
    search_fields = ('name', 'contact_person', 'industry')
    list_filter = ('industry', 'company_size')
    ordering = ('name',)
    prepopulated_fields = {"slug": ('name', )}
    date_hierarchy = 'created_at'  # Allows for date-based navigation

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.prefetch_related('users')  # Optimize queries with prefetch_related