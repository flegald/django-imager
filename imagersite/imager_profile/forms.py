"""Forms for user and profile."""
from imager_profile.models import ImagerProfile
from django.contrib.auth.models import User
from django.forms import ModelForm


class EditProfileForm(ModelForm):
    class Meta:
        model = ImagerProfile
        fields = ['location', 'bio', 'camera', 'photography_type']


class EditUserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
