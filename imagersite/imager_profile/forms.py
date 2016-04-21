"""Forms for profile and user."""
from django.forms import ModelForm
from .models import ImagerProfile
from django.contrib.auth.models import User


class EditProfileForm(ModelForm):
    """Edit profile form."""

    class Meta:
        model = ImagerProfile
        fields = ['location', 'bio', 'camera', 'photography_type']


class EditUserForm(ModelForm):
    """Edit user form."""

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']
