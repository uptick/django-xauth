# The views used below are normally mapped in django.contrib.admin.urls.py
# This URLs file is used to provide a reliable view deployment for test purposes.
# It is also provided as a convenience to those who want to deploy these URLs
# elsewhere.

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^password_change/$', views.password_change, name='password_change'),
]
