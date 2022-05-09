from django import forms


# class EntriesForm(forms.ModelForm):

    # class Meta:
    #     model = Artwork
    #     fields = ('artwork_title', 'medium')


class EntriesForm(forms.ModelForm):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

