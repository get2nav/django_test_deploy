from django import forms
from django.contrib.auth.models import User
from test_app.models import UserProfileInfo



class UserForm(forms.ModelForm):
    """docstring for F."""
    password = forms.CharField(widget = forms.PasswordInput())

    class Meta():
        """docstring for Meta."""
        model = User
        fields = ('username', 'email', 'password')


class UserProfileInfoForms(forms.ModelForm):
    """docstring for ."""
    class Meta():
        """docstring for Meta."""
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')
