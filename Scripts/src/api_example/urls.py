from django.conf.urls import url
from rest_framework import routers
from . import views
from django.urls import include, path

router = routers.DefaultRouter()
router.register('languages', views.LanguageView)

app_name = 'api_example'
urlpatterns = [
    path('', include(router.urls))
]
