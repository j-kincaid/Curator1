from django import forms

from .models import Artwork

class EntriesForm(forms.ModelForm):
    class Meta:
        model = Artwork
        fields = ('artwork_title', 'artwork_medium')