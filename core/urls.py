from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',
    url(r'^$', Home.as_view(), name='home'),
    url(r'^contact/create/$', ContactCreateView.as_view(), name='contact_create'),
    url(r'^success/$', Success.as_view(), name='success'),
)