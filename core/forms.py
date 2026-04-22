from django import forms
from django.conf import settings
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'email', 'event_type', 'event_date', 'event_time', 'venue', 'message']
        widgets = {
            'event_date': forms.DateInput(attrs={'type': 'date', 'placeholder': 'YYYY-MM-DD'}),
            'event_time': forms.TimeInput(attrs={'type': 'time', 'placeholder': 'HH:MM'}),
            'message': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Tell us about your event...'}),
        }