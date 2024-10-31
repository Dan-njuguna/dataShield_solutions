# decompyle3 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: C:\Users\Susan\OneDrive\Desktop\datashield solutions\Backend-Sys\authentication\forms.py
# Compiled at: 2024-10-29 14:57:18
# Size of source mod 2**32: 760 bytes
from django import forms
from .models import User, Organization

class UserRegistrationForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ["email","first_name","last_name","organization","password"]
        widgets = {"password": (forms.PasswordInput())}

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class OrganizationRegistrationForm(forms.ModelForm):

    class Meta:
        model = Organization
        fields =        ["name","address","contact_person","contact_email","contact_number","industry","company_size"]

# okay decompiling forms.cpython-38.pyc
