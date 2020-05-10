from django.shortcuts import render, get_object_or_404, redirect
from .models import Note, Profile
from .forms import NoteForm
from django.contrib.auth.models import User
from django.contrib.auth.views import login_required
from accounts.forms import MyFilter
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger

# Create your views here.

# <<---------------------------------------------------------------------------------------------------------->>
# <<------------------------------------------ Correct ------------------------------------------------------->>
def home(request):
    user= request.user
    profile = get_object_or_404(Profile, user = user)
    home_notes = Note.objects.all()
    filter = MyFilter(request.GET, queryset=home_notes)
    home_notes = filter.qs
    #<<---------------------------------Pagination--------------------------------------------------------------->>
    p = Paginator(home_notes, 2)
    page = request.GET.get('page')
    try:
        home_notes = p.page(page)
    except PageNotAnInteger:
        home_notes = p.page(1)
    except EmptyPage:
        home_notes = p.num_pages

    context = {
        'home_notes' : home_notes,
        'profile' : profile,
        'filter' : filter,
        'p' : p,
    }
    return render(request, 'home.html', context)

@login_required(login_url='accounts:login')
def user_notes(request):
    user=request.user
    user_notes = Note.objects.filter(user=user)
    filter = MyFilter(request.GET, queryset=user_notes)
    user_notes = filter.qs
    profile = get_object_or_404(Profile, user=user)
    context = {
        'user_notes' : user_notes,
        'profile' : profile,
        'filter' : filter,
    }
    return render(request, 'user_notes.html', context)

@login_required(login_url='accounts:login')
def one_note(request, slug, one_note_id):
    user = request.user
    profile = get_object_or_404(Profile, user = user)
    one_note = Note.objects.get(slug=slug, pk=one_note_id)
    context = {
        'one_note' : one_note,
        'profile' : profile,
    }
    return render(request, 'one_note.html', context)
@login_required(login_url='accounts:login')
def edit_note(request, slug, edit_id):
    user=request.user
    profile = get_object_or_404(Profile, user = user)
    note = get_object_or_404(Note,slug=slug, pk=edit_id)
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
        form = NoteForm(request.POST, request.FILES)
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

def delete(request, note_id):
    note = Note.objects.get(pk=note_id)
    if request.method == 'POST':
        note.delete()
        return redirect('/')
    context = {'note' : note,}
    return render(request, 'remove.html', context)