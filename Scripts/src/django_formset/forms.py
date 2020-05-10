from django import forms
from django.forms import formset_factory
from .models import *
from django.forms import BaseFormSet
class LanguageForm(forms.Form):
    name = forms.CharField(label='language',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter language\'s Name here'
        }))
    Programmer =  forms.CharField(
        label='Programmer',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Programmer\'s Name here'
        })
    )

class BaseArticleFormSet(BaseFormSet):
    def add_fields(self, form, index):
        super().add_fields(form, index)
        form.fields["new"] = forms.CharField()


f = formset_factory(LanguageForm, extra=3, formset=BaseArticleFormSet) #can_delete=True,

