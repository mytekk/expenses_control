from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<rok>[0-9]+)/(?P<miesiac>[0-9]+)/$', views.index, name='index'),
    url(r'^nowywydatek$', views.nowywydatek, name='nowywydatek'),
    url(r'^podaj_podkategorie/(?P<kat_id>[0-9]+)$', views.podaj_podkategorie, name='podaj_podkategorie'),
    url(r'^about$', views.about),
    url(r'^post$', views.post),
    url(r'^contact$', views.contact),
    ]
