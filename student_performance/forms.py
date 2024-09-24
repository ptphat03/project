from django import forms
from .models import StudentPerformance

# Form for creating and editing users
class StudentPerformanceForm(forms.ModelForm):
    class Meta:
        model = StudentPerformance
        fields = ['performance_id', 'user', 'test','score', 'feedback']
        widgets = {
            'test_id': forms.Select(attrs={'class': 'form-control'}),
        }
