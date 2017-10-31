# The views used below are normally mapped in django.contrib.admin.urls.py
# This URLs file is used to provide a reliable view deployment for test purposes.
# It is also provided as a convenience to those who want to deploy these URLs
# elsewhere.

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/$', views.login, name='ajax_login'),
    url(r'^logout/$', views.logout, name='ajax_logout'),
]
