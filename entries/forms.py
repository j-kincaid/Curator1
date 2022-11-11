from django import forms


class EntriesForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)
