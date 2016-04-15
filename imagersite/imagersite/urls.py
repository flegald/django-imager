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
from django.conf.urls import url
from django.contrib import admin

from .views import home_page, register_page, create_new_album #, album_display
# from ..imager_images.views import create_new_album
# out of toplevel package issue

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home_page, name='home_page'),
    url(r'^register/$', register_page, name='register_page'),
    url(r'^images/album/add/$', create_new_album, name='newalbum')
    # url(r'^images/photos/add/$', create_new_photo, name='newphoto')
    # url(r'^images/album/$', album_display, name='album')
    # url(r'^login', login_view, name='login'),
]
