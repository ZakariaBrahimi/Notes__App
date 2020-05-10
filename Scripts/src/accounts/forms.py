from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import django_filters
from django_filters import DateFilter
from Notes_app.models import Note


class MyFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name='created', lookup_expr='gte')
    end_date = DateFilter(field_name='created', lookup_expr='lte')
    class Meta:
        model = Note
        fields = ['title', 'active', 'tags']