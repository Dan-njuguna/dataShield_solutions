# decompyle3 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: C:\Users\Susan\OneDrive\Desktop\datashield solutions\Backend-Sys\audit_log\forms.py
# Compiled at: 2024-10-29 15:08:10
# Size of source mod 2**32: 302 bytes
from django import forms
from .models import AuditLog

class AuditLogForm(forms.ModelForm):

    class Meta:
        model = AuditLog
        fields = ["organization","user","action","action_description","affected_resource","ip_address","is_compliant","compliance_notes","additional_data"]

# okay decompiling forms.cpython-38.pyc
