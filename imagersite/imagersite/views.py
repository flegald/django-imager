"""Handle Imager views."""
from django.views.generic import TemplateView
from imager_images.models import Photo
from django.shortcuts import render, redirect
from .forms import UserForm, ProfileForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

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
            new_user = form.save()
            new_user.set_password(new_user.set_password)
            user = User.objects.get(email=new_user.email)
            import pdb; pdb.set_trace()
            login(request, user)
            return redirect('/registerdetail/')
    else:
        form = UserForm()
    return render(request, 'register.html', context={'form': form})


def detail_register_page(request):
    """Register page view."""
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            return redirect('/')
    else:
        form = ProfileForm()
    import pdb; pdb.set_trace()
    return render(request, 'registerdetail.html', context={'form': form})
