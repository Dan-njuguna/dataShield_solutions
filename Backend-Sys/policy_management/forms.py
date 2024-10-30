# decompyle3 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: C:\Users\Susan\OneDrive\Desktop\datashield solutions\Backend-Sys\policy_management\forms.py
# Compiled at: 2024-10-29 17:40:03
# Size of source mod 2**32: 889 bytes
from django import forms
from .models import Policy, PolicyVersion, ApprovalWorkflow

class PolicyForm(forms.ModelForm):

    class Meta:
        model = Policy
        fields = ('title', 'description', 'created_by', 'is_active')


class PolicyVersionForm(forms.ModelForm):

    class Meta:
        model = PolicyVersion
        fields = ('version_number', 'document', 'created_by')


class ApprovalWorkflowForm(forms.ModelForm):

    class Meta:
        model = ApprovalWorkflow
        fields = ('policy', 'approved_by', 'status')

    approved_at_display = forms.CharField(required=False,
      widget=forms.TextInput(attrs={"readonly": "readonly"}))

    def __init__(self, *args, **kwargs):
        (super().__init__)(*args, **kwargs)
        if self.instance.pk:
            self.fields["approved_at_display"].initial = self.instance.approved_at

# okay decompiling forms.cpython-38.pyc
