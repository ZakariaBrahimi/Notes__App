from django.shortcuts import render
from rest_framework import viewsets
from .models import Languages
from .serializers import LanguageSerializer
# Create your views here.

class LanguageView(viewsets.ModelViewSet):
    queryset = Languages.objects.all()
    serializer_class = LanguageSerializer
