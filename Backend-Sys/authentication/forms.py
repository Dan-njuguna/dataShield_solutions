import sys
sys.dont_write_bytecode = True
from django import forms
from .models import User, Organization

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), label="Password")
    confirm_password = forms.CharField(widget=forms.PasswordInput(), label="Confirm Password")

    class Meta:
        model = User
        fields = [
            "email",
            "first_name",
            "last_name",
            "organization",
            "phone_number",  # Added phone number
            "dark_mode",     # Added dark mode preference
            "password",
        ]

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class OrganizationRegistrationForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = [
            "name",
            "address",  # Added address field
            "contact_person",
            "contact_email",
            "contact_number",
            "industry",
            "company_size",
        ]

    def clean_contact_email(self):
        contact_email = self.cleaned_data.get("contact_email")
        if Organization.objects.filter(contact_email=contact_email).exists():
            raise forms.ValidationError("This contact email is already in use.")
        return contact_email