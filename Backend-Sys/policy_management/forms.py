import sys
sys.dont_write_bytecode = True
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

