from django import forms
from django.core import validators


class FormName(forms.Form):
    """docstring for F."""
    name = forms.CharField()
    email = forms.EmailField()
    verify = forms.EmailField()
    text = forms.CharField(widget = forms.Textarea)


    def clean(self):
        all_clean_data = super().clean()
        email_data = all_clean_data['email']
        verify_data = all_clean_data['verify']

        if email_data != verify_data:
            raise forms.ValidationError(" Email not matching ")
