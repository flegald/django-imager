"""Forms for albums and photos."""

from django.forms import ModelForm
from imager_images.models import Photo, Album


class NewAlbumForm(ModelForm):
    class Meta:
        model = Album
        fields = ['title', 'description']


class NewPhotoForm(ModelForm):
    class Meta:
        model = Photo
        fields = ['title', 'description', 'img_file']
