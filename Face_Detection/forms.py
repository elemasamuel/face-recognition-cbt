from django import forms
from .models import *

class ResgistrationForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'reg_number',
            'name',

        ]