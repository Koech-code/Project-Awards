from . import views
from django.conf.urls import url
from django.contrib.auth.views import LogoutView


urlpatterns=[
    url('^$', views.index, name='index')
]