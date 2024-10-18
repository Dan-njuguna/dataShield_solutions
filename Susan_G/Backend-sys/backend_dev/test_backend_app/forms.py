from django import forms
from .models import User, Organization, ComplianceStatus, DataProtectionRegulation, Gdpr4, KenyaDPA


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'organization', 'password']

class OrganizationCreationForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = [
            'name',
            'address',
            'contact_person',
            'contact_email',
            'contact_number',
            'industry',
            'company_size',
        ]
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter organization name'}),
            'address': forms.TextInput(attrs={'placeholder': 'Enter organization address'}),
            'contact_person': forms.TextInput(attrs={'placeholder': 'Enter contact person name'}),
            'contact_email': forms.EmailInput(attrs={'placeholder': 'Enter contact email'}),
            'contact_number': forms.TextInput(attrs={'placeholder': 'Enter contact number'}),
            'industry': forms.TextInput(attrs={'placeholder': 'Enter industry type'}),
            'company_size': forms.TextInput(attrs={'placeholder': 'Enter company size'}),
        }

class ComplianceStatusForm(forms.ModelForm):
    class Meta:
        model = ComplianceStatus
        fields = ['compliance_status', 'organization', 'data_protection_regulations']

class DataProtectionRegulationForm(forms.ModelForm):
    class Meta:
        model = DataProtectionRegulation
        fields = ['name', 'jurisdiction', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
            'jurisdiction': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }

class KenyaDPAForm(forms.ModelForm):
    class Meta:
        model = KenyaDPA
        fields = ['data_protection_regulation', 'category', 'description', 'section_in_act', 'key_points']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
            'key_points': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }



class Gdpr4Form(forms.ModelForm):
    class Meta:
        model = Gdpr4
        fields = ['category', 'description', 'gdpr_articles', 'recitals', 'data_protection_regulation']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
            'gdpr_articles': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
            'recitals': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }