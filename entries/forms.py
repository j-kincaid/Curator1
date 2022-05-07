from django import forms

class EntriesForm(forms.ModelForm):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

