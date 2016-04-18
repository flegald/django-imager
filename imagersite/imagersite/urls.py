"""imagersite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView, DetailView
from .views import home_page, profile_view
from imager_images.models import Album, Photo


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home_page, name='home_page'),
    url(r'^accounts/', include('registration.backends.hmac.urls')),
    url(r'^accounts/profile', profile_view, name='profile_view'),
    url(r'^images/library/$', TemplateView.as_view(template_name="library.html")),

    url(r'^images/album/(?P<pk>[0-9]+)/$',
        DetailView.as_view(model=Album, template_name="album.html")),
    url(r'^images/photo/(?P<pk>[0-9]+)/$',
        DetailView.as_view(model=Photo, template_name="photo.html")),
    ]

