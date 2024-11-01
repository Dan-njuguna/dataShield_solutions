
from django import forms
from .models import AuditLog

class AuditLogForm(forms.ModelForm):

    class Meta:
        model = AuditLog
        fields = ["organization","user","action","action_description","affected_resource","ip_address","is_compliant","compliance_notes","additional_data"]

