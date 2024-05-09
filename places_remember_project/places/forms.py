from django import forms
from .models import Memory


class MemoryForm(forms.ModelForm):
    class Meta:
        model = Memory
        fields: list[str] = ['title', 'location',
                             'comment', 'latitude', 'longitude']
