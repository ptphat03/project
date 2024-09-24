from django import forms
from .models import User

# Form for creating and editing users
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['user_id','username', 'email', 'full_name']

