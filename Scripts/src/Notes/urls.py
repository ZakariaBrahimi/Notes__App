"""Notes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView, LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView,  PasswordResetCompleteView


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', include('Notes_app.urls', namespace='home')),
    path('', include('accounts.urls', namespace='accounts')),
    path('', include('api_example.urls', namespace='api')),
    path('', include('django_formset.urls', namespace='fomset')),
    

    
    # path('accounts/', include('django.contrib.auth.urls')), Everything About User log in / out and reset password's user  
    url(r'^login/$', LoginView.as_view(template_name='registrations/login.html'), name='login'),
    url(r'^logout/$', LogoutView.as_view() , name='logout'),
    url(r'^password_change/$', PasswordChangeView.as_view(template_name='registrations/password_change_form.html') , name='password_change'),
    url(r'^password_change_done/$', PasswordChangeDoneView.as_view(template_name='registrations/password_change_done.html') , name='password_change_done'),
    url(r'^reset_password/$', PasswordResetView.as_view(template_name='registrations/password_reset_form.html') , name='password_reset'),
    url(r'^reset_password_sent/$', PasswordResetDoneView.as_view(template_name='registrations/password_reset_done.html') , name='password_reset_done'),
    url(r'^reset/<uidb64>/<token>$', PasswordResetConfirmView.as_view(template_name='registrations/password_reset_confirm.html') , name='password_reset_confirm'),
    url(r'^reset_password_complete$', PasswordResetCompleteView.as_view(template_name='registrations/password_reset_complete.html') , name='password_reset_complete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)