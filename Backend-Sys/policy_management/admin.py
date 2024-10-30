# decompyle3 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: C:\Users\Susan\OneDrive\Desktop\datashield solutions\Backend-Sys\policy_management\admin.py
# Compiled at: 2024-10-29 15:31:23
# Size of source mod 2**32: 366 bytes
from django.contrib import admin
from .models import Policy, PolicyVersion, ApprovalWorkflow

class PolicyAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'is_active', 'created_by')
    prepopulated_fields = {"slug": ('title', )}


admin.site.register(Policy)
admin.site.register(PolicyVersion)
admin.site.register(ApprovalWorkflow)

# okay decompiling admin.cpython-38.pyc
