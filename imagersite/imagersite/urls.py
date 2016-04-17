"""imagersite URL Configuration.

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
<<<<<<< HEAD
from .views import home_page, register_page, detail_register_page
from django.conf import settings
from django.conf.urls import patterns
=======

from .views import home_page
>>>>>>> b42a3fab79fc330db9e13f4581d731039b8eda46

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home_page, name='home_page'),
<<<<<<< HEAD
    url(r'^register/$', register_page, name='register_page'),
    url(r'^registerdetail/$', detail_register_page, name='register_detail_page'),
=======
    url(r'^accounts/', include('registration.backends.hmac.urls')),
    # url(r'^login', login_view, name='login'),
>>>>>>> b42a3fab79fc330db9e13f4581d731039b8eda46
]


if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT,
        }),
    )


