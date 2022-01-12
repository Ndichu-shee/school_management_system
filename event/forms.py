from django import forms
from django.db.models import fields
from .models import Event

class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = '__all__'