import sys
sys.dont_write_bytecode = True
from django.contrib import admin
from .models import Policy, PolicyVersion, ApprovalWorkflow

class PolicyAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'is_active', 'created_by')
    prepopulated_fields = {"slug": ('title', )}


admin.site.register(Policy)
admin.site.register(PolicyVersion)
admin.site.register(ApprovalWorkflow)


