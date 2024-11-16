import sys
sys.dont_write_bytecode = True
from django.contrib import admin
from .models import AuditLog

@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    list_display = ('action', 'affected_resource', 'user', 'organization', 'created_at',
                    'is_compliant')
    search_fields = ('action', 'affected_resource', 'user__email', 'organization__name')
    list_filter = ('action', 'is_compliant', 'organization')
    ordering = ('-created_at', )

