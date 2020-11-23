from django import forms
from .models import Note
class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = '__all__'
        # TODO: exclude= ['user']
        # exclude = ['img']
        # don't forget this

