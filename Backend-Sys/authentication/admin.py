# decompyle3 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: C:\Users\Susan\OneDrive\Desktop\datashield solutions\Backend-Sys\authentication\admin.py
# Compiled at: 2024-10-29 15:00:31
# Size of source mod 2**32: 615 bytes
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

# okay decompiling admin.cpython-38.pyc
