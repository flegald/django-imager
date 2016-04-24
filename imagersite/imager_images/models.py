"""Models to handle photos and their albums."""
from django.db import models as md
from django.conf import settings
from django.utils.encoding import python_2_unicode_compatible
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


PUB_CHOICE = [('Private', 'Private'),
                ('Shared', 'Shared'),
                ('Public', 'Public')]

@python_2_unicode_compatible
class Photo(md.Model):
    """Single image model."""

    owner = md.ForeignKey(settings.AUTH_USER_MODEL,
                            related_name='photos',
                            null=True, blank=True)
    title = md.CharField(default='', max_length=255, null=True, blank=True)
    description = md.CharField(default='', max_length=255, null=True, blank=True)
    date_uploaded = md.DateTimeField(auto_now_add=True)
    date_modified = md.DateTimeField(auto_now_add=True)
    date_published = md.DateTimeField(auto_now_add=True)
    published = md.CharField(max_length=255, choices=PUB_CHOICE,
                            default='Private')
    img_file = md.ImageField(upload_to='img_files')
    in_album = md.ManyToManyField('Album', related_name='photos')

    def __str__(self):
        """Return string of title."""
        return self.title

    def get_url(self):
        """Return string of url for single view."""
        return 'media/{}'.format(self.img_file)



@python_2_unicode_compatible
class Album(md.Model):
    """Album to house images."""

    owner = md.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=md.CASCADE,
                              related_name='albums',
                              null=True)
    cover = md.ImageField(default='img_files/upload.png')
    title = md.CharField(default='', max_length=255, null=True, blank=True)
    description = md.TextField(default='', null=True, blank=True)
    date_uploaded = md.DateTimeField(auto_now_add=True)
    date_modified = md.DateTimeField(auto_now=True)
    date_published = md.DateTimeField(auto_now_add=True)
    published = md.CharField(max_length=255, choices=PUB_CHOICE,
                                 default='Private')


    def __str__(self):
        return self.title
