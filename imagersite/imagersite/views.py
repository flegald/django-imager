"""Handle Imager views."""
from django.views.generic import TemplateView
from imager_images.models import Photo
from django.shortcuts import render, redirect
from .forms import UserForm, ProfileForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
import settings

import os


def home_page(request):
    """Home page view."""
    try:
        img = Photo.objects.all().filter(published='public').order_by("?")[0].photo
    except IndexError:
        img = 'http://purplewalls.com/wp-content/uploads/2016/03/happy-dog-image-93.jpg'
    return render(request, 'home.html', context={'img': img})


def register_page(request):
    """Register page view."""
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(username=form.data['username'], email=form.data['email'], password=form.data['csrfmiddlewaretoken'],)
            new_user.save()
            new_user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, new_user)
            return redirect('/registerdetail')
    else:
        form = UserForm()
    return render(request, 'register.html', context={'form': form})


def detail_register_page(request):
    """Register page view."""
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            user = request.user.profile
            user.location = form.data['location']
            user.bio = form.data['bio']
            user.camera = form.data['camera']
            import pdb; pdb.set_trace()
            return redirect('/')
    else:
        form = ProfileForm()
    return render(request, 'registerdetail.html', context={'form': form})
