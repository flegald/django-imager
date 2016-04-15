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


def register_page(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(username=form.data['username'], email=form.data['email'], password=form.data['csrfmiddlewaretoken'],)
            new_user.save()
            new_user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, new_user)
            import pdb; pdb.set_trace()
            return redirect('/')
    else:
        sign_up_form = RegistrationForm()
        return render(request, 'register.html', context={
            'sign_up_form': sign_up_form
        })


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


# def album_display(request):
#     albums = Album.add
