"""Image type forms."""
from django.forms import ModelForm
from .models import Photo, Album


class NewAlbumForm(ModelForm):
    """Form for new album."""

    class Meta:
        model = Album
        fields = ['title', 'description']


class NewPhotoForm(ModelForm):
    """Form for new photo."""

    class Meta:
        model = Photo
        fields = ['title', 'description', 'img_file']
