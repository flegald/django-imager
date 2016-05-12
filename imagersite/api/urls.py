"""Urls for accessing the Imager data through REST API."""
from django.conf.urls import url
from api import views


urlpatterns = [
    url(r'^photos/$', views.PhotoListView.as_view(), name='photos'),
    url(r'^albums/$', views.AlbumListView.as_view(), name='photos'),
]
