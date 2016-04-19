# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django import forms
# from .models import PUB_CHOICE
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, render_to_response, redirect
from django.views.generic import TemplateView
from registration.forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from imager_images.models import Photo, Album
from django.contrib.auth.models import User


def home_page(request):

    try:
        img = Photo.objects.all().filter(published='public').order_by("?")[0].photo
    except IndexError:
        img = 'http://purplewalls.com/wp-content/uploads/2016/03/happy-dog-image-93.jpg'

    log_in_form = AuthenticationForm()
    return render(request, 'home.html', context={
        'img': img,
        'login': log_in_form
    })


def profile_view(request):
    """Set up profile view."""
    if request.user.is_authenticated():
        image_count = len(request.user.photos.all())
        album_count = len(request.user.albums.all())
        return render(request, 'profile_view.html', context={'image_count': image_count, 'album_count': album_count})


def library(request):
    """Set up librabry view."""
    photos = []
    for photo in request.user.photos.all():
        photos.append(photo.img_file)
    return render(request, 'library.html', context={'photos': photos})


PUB_CHOICE = [('Private', 'Private'),
              ('Shared', 'Shared'),
              ('Public', 'Public')]


class NewAlbumForm(forms.Form):
    title = forms.CharField(label='Title', initial='untitled')
    description = forms.CharField(widget=forms.Textarea(), label='Description')
    privacy = forms.ChoiceField(widget=forms.RadioSelect(),
                                label='Privacy',
                                choices=PUB_CHOICE,
                                initial='Public')


def create_new_album(request):
    new_album_form = NewAlbumForm()
    return render(request, 'newalbum.html', context={
        'new_album_form': new_album_form
    })


class NewPhotoForm(forms.Form):
    title = forms.CharField(label='Title', initial='untitled')
    description = forms.CharField(widget=forms.Textarea(), label='Description')
    privacy = forms.ChoiceField(widget=forms.RadioSelect(),
                                label='Privacy',
                                choices=PUB_CHOICE,
                                initial='Public')


def upload_new_photo(request):
    new_photo_form = NewPhotoForm()
    return render(request, 'newphoto.html', context={
        'new_photo_form': new_photo_form
    })
