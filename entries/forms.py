from django import forms

from .models import Artwork

class ArtworkForm(forms.ModelForm):
    class Meta:
        model = Artwork
        fields = ('artwork_title', 'medium', 'height_in_inches', 'width_in_inches', 'depth_in_inches', 'year_completed',)
    # name = forms.CharField()
    # message = forms.CharField(widget=forms.Textarea)

