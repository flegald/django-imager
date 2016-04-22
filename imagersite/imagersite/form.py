from django.forms import ModelForm
from imager_images.models import Photo, Album
from imager_profile.models import ImagerProfile
from django.contrib.auth.models import User


class NewAlbumForm(ModelForm):
    class Meta:
        model = Album
        fields = ['title', 'description']


class NewPhotoForm(ModelForm):
    class Meta:
        model = Photo
        fields = ['title', 'description', 'img_file']


class EditProfileForm(ModelForm):
    class Meta:
        model = ImagerProfile
        fields = ['location', 'bio', 'camera', 'photography_type']


class EditUserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class EditPhotoForm(ModelForm):
    class Meta:
        model = Photo
        fields = ['title', 'description']
