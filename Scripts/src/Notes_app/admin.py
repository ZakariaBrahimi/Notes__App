from django.contrib import admin
from .models import Note, Profile
# Register your models here.

class NotesAdmin(admin.ModelAdmin):
    list_filter = ['active', 'created','img']
    list_display = ['user','title', 'created', 'active','img']
    search_fields = ['title', 'content']
    list_editable = ['active']

admin.site.register(Note, NotesAdmin)
admin.site.register(Profile)
