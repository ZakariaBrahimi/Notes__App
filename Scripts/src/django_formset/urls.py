from django.conf.urls import url
from . import views 
app_name = 'django_formset'

urlpatterns = [
    url(r'^formset/$', views.formset, name='formset'),
    url(r'^model_formset/$', views.modelformset, name='model_formset'),
    url(r'^inline_formset/$', views.modelformset, name='inline_formset'),
]
