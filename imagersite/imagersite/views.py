# -*- coding: utf-8 -*-
"""Views handler."""

from __future__ import unicode_literals
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, render_to_response, redirect
from django.views.generic import TemplateView
from registration.forms import RegistrationForm
from django.contrib.auth import authenticate, login
from registration.backends.hmac.views import RegistrationView

from django.contrib.auth.forms import AuthenticationForm
from imager_images.models import Photo, Album
from django.contrib.auth.models import User


def home_page(request):
    """Home page view with login."""
    try:
        img = Photo.objects.all().filter(published='public').order_by("?")[0].photo
    except IndexError:
        img = 'http://orig14.deviantart.net/38de/f/2014/003/c/5/work_harder_comrade__by_pallanoph-d5kk9qt.jpg'

    name = request.user.username
    return render(request, 'home.html', context={
        'img': img,
        'name': name
    })


def library(request):
    albums = []
    for album in request.user.albums.all():
        albums.append(album.cover.url[1:])
    return render(request, 'images/library.html', context={'albums': albums})


def profile_view(request):
    if request.user.is_authenticated():
        try:
            img = Photo.objects.all().filter(owner=request.user.profile.user).order_by("?")[0].photo.url
        except IndexError:
            img = 'http://lorempixel.com/400/200/'
        image_count = len(request.user.photos.all())
        album_count = len(request.user.albums.all())
        return render(request, 'profile_view.html', context={'img': img, 'image_count': image_count, 'album_count': album_count})
    else:
        return redirect('login')
