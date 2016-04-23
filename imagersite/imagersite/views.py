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
from .settings import MEDIA_ROOT
from django.contrib.auth.forms import AuthenticationForm
from imager_images.models import Photo, Album
from imager_profile.models import ImagerProfile
from django.contrib.auth.models import User
from .settings import MEDIA_ROOT
from django.views.generic.edit import UpdateView
from django.contrib.auth.decorators import login_required
import datetime
from .form import NewAlbumForm, NewPhotoForm, EditProfileForm, EditUserForm, EditPhotoForm


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


@login_required(redirect_field_name='/')
def profile_view(request):
    """Set up profile view."""
    dbuser = User.objects.get(pk=request.user.id)
    if request.user.is_authenticated():
        image_count = len(request.user.photos.all())
        album_count = len(request.user.albums.all())
        return render(request, 'profile_view.html', context={'image_count': image_count, 'album_count': album_count, 'dbuser': dbuser})


@login_required(redirect_field_name='/')
def create_new_album(request):
    """Create new album."""
    user = User.objects.get(pk=request.user.id)
    if request.method == 'POST':
        form = NewAlbumForm(request.POST)
        album = Album(title=form.data['title'], description=form.data['description'])
        album.save()
        user.albums.add(album)
        return redirect('/images/library/')
    elif request.method == 'GET':
        new_album_form = NewAlbumForm()
        return render(request, 'newalbum.html', context={
            'new_album_form': new_album_form
    })


@login_required(redirect_field_name='/')
def upload_new_photo(request):
    """Upload new photo."""
    user = User.objects.get(pk=request.user.id)
    if request.method == 'GET':
        new_photo_form = NewPhotoForm()
        return render(request, 'newphoto.html', context={
            'new_photo_form': new_photo_form
        })
    elif request.method == 'POST':
        new_photo = NewPhotoForm(request.POST, request.FILES)
        photo = Photo(title=new_photo.data['title'], description=new_photo.data['description'], img_file=request.FILES['img_file'])
        photo.save()
        user.photos.add(photo)
        return redirect('/images/library/')


@login_required(redirect_field_name='/')
def edit_profile(request):
    user = User.objects.get(pk=request.user.id)
    if request.method == 'POST':
        prof_form = EditProfileForm(request.POST, instance=user.profile)
        usr_form = EditUserForm(request.POST, instance=user)
        if prof_form.is_valid() and usr_form.is_valid():
            prof_form.save()
            usr_form.save()
            return redirect("/accounts/profile")
    elif request.method == 'GET':
        profile_edit = EditProfileForm(instance=request.user.profile)
        user_edit = EditUserForm(instance=request.user)
        return render(request, 'profile_edit.html', context={'profile_edit':profile_edit, 'user_edit': user_edit})


class Edit_Photo(UpdateView):
    """A form to edit photos."""

    model = Photo
    fields = ['title', 'description', 'published']
    template_name = 'photo_update_form.html'
    success_url = '/images/library/'

    def form_valid(self, form):
        """Validate form."""

        form.instance.date_modified = datetime.datetime.now()
        return super(Edit_Photo, self).form_valid(form)

