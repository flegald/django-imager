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
from django.conf.urls import url, include, patterns
from django.views.generic import TemplateView, DetailView
from .views import home_page, library
from imager_images.models import Album, Photo
from django.conf import settings
from django.conf.urls.static import static
from imager_images.views import create_new_album, Upload_Photo, Edit_Photo, Edit_Album
from imager_profile.views import edit_profile, profile_view
from django.contrib import admin
from django.views.generic import DetailView
from imager_images.models import Photo, Album
from django.contrib import admin
from django.contrib.auth.decorators import login_required



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home_page, name='home_page'),

    # Account urls
    url(r'^accounts/', include('registration.backends.hmac.urls')),
    url(r'^accounts/profile', profile_view, name='profile_view'),
    url(r'^profile/edit/$', edit_profile, name='profile_edit'),
    # Image urls
    url(r'^images/library/$', library, name='library'),
    url(r'^images/album/(?P<pk>[0-9]+)/$',
        DetailView.as_view(model=Album, template_name="detail_album.html")),
    url(r'^images/photo/(?P<pk>[0-9]+)/$',
        DetailView.as_view(model=Photo, template_name="detail_photo.html")),
    url(r'^images/album/add/$', create_new_album, name='newalbum'),
    url(r'^images/photos/add/$',
        login_required(Upload_Photo.as_view()), name='newphoto'),
    url(r'^images/photos/(?P<pk>[0-9]+)/edit/$',
        login_required(Edit_Photo.as_view()), name='editphoto'),
    url(r'^images/album/(?P<pk>[0-9]+)/edit/$',
        login_required(Edit_Album.as_view()), name='editalbum')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$',
            'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, }),
    )
