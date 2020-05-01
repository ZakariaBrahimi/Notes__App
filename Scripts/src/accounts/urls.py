from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView
app_name = 'accounts'
urlpatterns = [
    url(r'^login/$', LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^logout/$', LogoutView.as_view() , name='logout'),
]
