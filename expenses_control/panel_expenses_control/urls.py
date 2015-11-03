from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<rok>[0-9]+)/(?P<miesiac>[0-9]+)/$', views.index, name='index'),
    ]
