from django.conf.urls import url
from . import views
from django.contrib.auth.views import LoginView,LogoutView
app_name = 'Notes_app'
urlpatterns = [
    url(r'^$', views.home, name='home_page'),
    url(r'^user_notes/$', views.user_notes, name='user_notes'),
    url(r'^one_note/(?P<slug>[-\w]+)/(?P<one_note_id>\d+)/$', views.one_note, name='one_note'),
    url(r'^add_note/$', views.add_note, name='add_note'),
    url(r'^edit_note/(?P<slug>[-\w]+)/(?P<edit_id>\d+)/$', views.edit_note, name='edit_note'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^delete/(?P<note_id>\d+)/$', views.delete, name='delete'),
    
    
    
]