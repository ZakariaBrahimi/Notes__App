from django.shortcuts import render, get_object_or_404, redirect
from .models import Note, Profile
from .forms import NoteForm
from django.contrib.auth.models import User
from django.contrib.auth.views import login_required

# Create your views here.

# <<---------------------------------------------------------------------------------------------------------->>
# <<------------------------------------------ Correct ------------------------------------------------------->>
def home(request):
    # user= request.user
    # profile = get_object_or_404(Profile, user = user)
    home_notes = Note.objects.all()
    context = {
        'home_notes' : home_notes,
        'profile' : profile,
    }
    return render(request, 'home.html', context)

@login_required(login_url='accounts:login')
def user_notes(request):
    user=request.user
    user_notes = Note.objects.filter(user=user)
    profile = get_object_or_404(Profile, user=user)
    context = {
        'user_notes' : user_notes,
        'profile' : profile,
    }
    return render(request, 'user_notes.html', context)

@login_required(login_url='accounts:login')
def one_note(request, slug, one_note_id):
    user = request.user
    profile = get_object_or_404(Profile, user = user)
    one_note = Note.objects.get(slug__exact=slug, pk=one_note_id)
    context = {
        'one_note' : one_note,
        'profile' : profile,
    }
    return render(request, 'one_note.html', context)
@login_required(login_url='accounts:login')
def edit_note(request, slug, edit_id):
    user=request.user
    profile = get_object_or_404(Profile, user = user)
    note = Note.objects.get(slug=slug, pk=edit_id)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            # slug = slug
            # edit_id = note.id
            #url = f"one_note/{slug}/{edit_id}"
            return redirect('home:one_note', note.slug, note.id)
    else:
        form = NoteForm(instance=note)
    context = {
        'form' : form,
        'profile' : profile,
    }
    return render(request, 'edit_note.html', context)
@login_required(login_url='accounts:login')
def add_note(request):
    user=request.user
    profile = get_object_or_404(Profile, user = user)
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = NoteForm()
    context = {
        'form' : form,
        'profile' : profile,
    }
    return render(request, 'add_note.html', context)
# <<---------------------------------------------------------------------------------------------------------->>
#<<----------------------------------------------------------------------------------------------------------->>
@login_required(login_url='accounts:login')
def profile(request):
    user=request.user
    profile = get_object_or_404(Profile, user = user)
    #profile_notes = Note.objects.filter(user=user)
    context = {
        'profile' : profile,
    }
    return render(request, 'profile.html', context)
