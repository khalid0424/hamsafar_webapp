from django import forms
from .models import Hamsafar

class HamsafarForm(forms.ModelForm):
    class Meta:
        model = Hamsafar
        fields = ['name', 'start_location', 'destination', 'date', 'seats', 'description']
