from django import forms
from .models import Partne

class partnerform(forms.ModelForm):
    class Meta:
        model = Partne
        fields = ('firstname', 'lastname','email', 'address', 'interest', 'biodata', 'acceptancenote')