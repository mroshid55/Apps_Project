from .models import *
from django import forms


class NotesForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(
        attrs={"rows": 2, "cols": 20}), max_length=100)

    class Meta:
        model = Note
        fields = ('title', 'description', 'tags', 'favourites')
