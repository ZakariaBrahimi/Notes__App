from django.conf.urls import url
from django.urls import path,include
from . import views
app_name = 'accounts'    
urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    
]
