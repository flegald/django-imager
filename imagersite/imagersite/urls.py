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
from .views import home_page, create_new_album, profile_view, library
from django.contrib.auth.decorators import login_required
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.views.generic import TemplateView, DetailView
from imager_images.models import Photo, Album

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home_page, name='home_page'),
    url(r'^accounts/', include('registration.backends.hmac.urls')),
    url(r'^accounts/profile', profile_view, name='profile_view'),
    url(r'^images/library/$', library, name="library.html"),
    url(r'^images/album/add/$', create_new_album, name='newalbum')
    url(r'^images/photos/add/$', upload_new_photo, name='newphoto')
    # url(r'^images/album/$', album_display, name='album')
    # url(r'^login', login_view, name='login'),


    # url(r'^images/album/(?P<pk>[0-9]+)/$',
    #     DetailView.as_view(model=Album, template_name="album.html")),
    # url(r'^images/photo/(?P<pk>[0-9]+)/$',
    #     DetailView.as_view(model=Photo, template_name="photo.html")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL,
#                           document_root=settings.STATIC_ROOT)
