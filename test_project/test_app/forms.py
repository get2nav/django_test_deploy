from django import forms
from test_app.models import User



class NewUserForm(forms.ModelForm):
    """docstring for F."""

    class Meta():
        """docstring for Meta."""
        model = User
        fields = '__all__'
