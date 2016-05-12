"""Views for profile and user."""
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from imager_profile.forms import EditProfileForm, EditUserForm
from django.shortcuts import redirect


@login_required(redirect_field_name='/')
def edit_profile(request):
    """Edit profile view."""
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


@login_required(redirect_field_name='/')
def profile_view(request):
    """Set up profile view."""
    dbuser = User.objects.get(pk=request.user.id)
    if request.user.is_authenticated():
        image_count = len(request.user.photos.all())
        album_count = len(request.user.albums.all())
        return render(request, 'profile_view.html', context={'image_count': image_count, 'album_count': album_count, 'dbuser': dbuser})