from django import forms
from .models import TestGroup, Test

# Form for creating and editing users
class TestGroupForm(forms.ModelForm):
    class Meta:
        model = TestGroup
        fields = ['test_group_id','test_group_name', 'weight']
    
class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = ['test_id','test_name','course','test_group']