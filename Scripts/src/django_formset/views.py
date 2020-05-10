from django.shortcuts import render, redirect
from django.forms import formset_factory,modelformset_factory, inlineformset_factory
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Language, Programmer
from .forms import f
# Create your views here.

def formset(request):
    if request.method == 'POST':
# Django will become valid even if an empty form is submitted. Adding initial data causes unbound form and trigger formset.errors
        formset = f(request.POST, initial = [{'name': '.', 'Programmer': '.'}])
        if formset.is_valid():
            for form in formset:
                name = form.cleaned_data.get('name')
                Programmer = form.cleaned_data.get('Programmer')
                if name and Programmer:
                    Language(name=name, Programmer=Programmer).save()
            return redirect('/')
    else:
        formset = f()
    
    context = {
        'formset' : formset,
    }
    return render(request, 'formset.html', context)

def modelformset(request):
    language_formset = modelformset_factory(
        Language,
        fields =['name', 'Programmer'],
        extra=2,
        # queryset=Language.objects.filter(name__startswith='p')  #queryset=Language.objects.none(),
        # widgets={'name': Textarea(attrs={'cols': 80, 'rows': 20})},
        # localized_fields=('__all__')
        # initial = [{'name': 'mama ','programmer': 'mama'},
        #            {'name': 'ayoube ','programmer': 'ayoube'}]
        )
    if request.method == 'POST':
        formset = language_formset(request.POST)
        if formset.is_valid():
            formset.save()
            return redirect('/')
    else:
        formset = language_formset()
    context = {
        'model_formset' : formset,
    }
    return render(request, 'modelformset.html', context)




def inlineformset(request):
    context = {}
    return render(request, 'inline_formset.html', context)
