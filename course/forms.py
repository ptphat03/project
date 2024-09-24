from django import forms
from .models import Course

# Form for creating and editing users
class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_id', 'course_name','course_description', 'created_by']
        widgets = {
            'course_name': forms.TextInput(attrs={'class': 'form-control'}),
            'course_description': forms.Textarea(attrs={'class': 'form-control'}),
        }