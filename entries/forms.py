from django import forms
from .models import Artwork
from django.db.models.base import Model
from django.forms import ModelForm, widgets


class EntriesForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)


class ArtworkForm(ModelForm):
    class Meta:
        model = Artwork
        fields = [
            "artwork_title",
            "featured_image",
            "description",
            "demo_link",
            "tags",
        ]
        widgets = {
            "tags": forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super(ArtworkForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({"class": "input"})
