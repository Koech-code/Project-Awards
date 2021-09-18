from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns=[
    url('^$', views.index, name='index'),
    url('profile/' ,views.profile, name='profile'),
    url(r'^api/projects/$', views.ProjList.as_view()),
    url(r'^api/profiles/$', views.ProfList.as_view()),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
