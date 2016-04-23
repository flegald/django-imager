# -*- coding: utf-8 -*-
"""Views handler."""

from __future__ import unicode_literals
from django.shortcuts import render
from imager_images.models import Photo
from django.contrib.auth.decorators import login_required
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


@login_required(redirect_field_name='/')
def library(request):
    """Set up library view."""
    user = User.objects.get(pk=request.user.id)
    return render(request, 'library.html', context={'photos': user.photos.all(), 'albums': user.albums.all()})

