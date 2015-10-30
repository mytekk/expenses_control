#from django.conf.urls.defaults import *
from django.conf.urls import *

from . import views

urlpatterns = patterns('flexselect.views',
    (r'field_changed', 'field_changed'),
)
