from django.forms import ModelForm
from imager_profile.models import ImagerProfile
from django.contrib.auth.models import User


class UserForm(ModelForm):
    """Create basic User form."""

    class Meta:
        model = User

        fields = ['username', 'email', 'password']


class ProfileForm(ModelForm):
    """Create ImagerProfile form."""

    class Meta:
        model = ImagerProfile

        fields = ['location', 'bio', 'camera', 'photography_type']
        exclude = ['friends', 'user']
