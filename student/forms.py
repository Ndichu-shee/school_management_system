from django import forms
from django.db.models import fields
from .models import Student
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'