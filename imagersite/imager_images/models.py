"""Models to handle photos and their albums."""
from django.db import models as md
from django.conf import settings

PUB_CHOICE = [('Private', 'Private'),
                ('Shared', 'Shared'),
                ('Public', 'Public')]


class Photo(md.Model):
    """Single image model."""

    owner = md.ForeignKey(settings.AUTH_USER_MODEL,
                            related_name='photos')
    title = md.CharField(default='', max_length=255)
    description = md.CharField(default='', max_length=255)
    date_uploaded = md.DateTimeField(auto_now_add=True)
    date_modified = md.DateTimeField(auto_now_add=True)
    date_published = md.DateTimeField(auto_now_add=True)
    published = md.CharField(max_length=7, choices=PUB_CHOICE,
                            default='Private')
    img_file = md.ImageField(upload_to='img_files')
    in_album = md.ManyToManyField('Album', related_name='photos')

    def __str__(self):
        """Return string of title."""
        return self.title


class Album(md.Model):
    """Photo album model."""

    owner = md.ForeignKey(settings.AUTH_USER_MODEL,
                            related_name='albums')
    title = md.CharField(default='', max_length=255)
    description = md.CharField(default='', max_length=255)
    date_uploaded = md.DateTimeField(auto_now_add=True)
    date_modified = md.DateTimeField(auto_now_add=True)
    date_published = md.DateTimeField(auto_now_add=True)
    published = md.CharField(max_length=255, choices=PUB_CHOICE,
                            default='Private')
    contains = md.ManyToManyField('Photo', related_name='albums')

    def __str__(self):
        """Return string of title."""
        return self.title
