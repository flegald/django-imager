"""Models to handle photos and their albums."""
from django.db import models as md
from django.conf import settings
from django.utils.encoding import python_2_unicode_compatible


PUB_CHOICE = [('Private', 'Private'),
                ('Shared', 'Shared'),
                ('Public', 'Public')]

@python_2_unicode_compatible
class Photo(md.Model):
    """Single image model."""

    owner = md.ForeignKey(settings.AUTH_USER_MODEL,
                            related_name='photos')
    title = md.CharField(default='', max_length=255)
    description = md.CharField(default='', max_length=255)
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
        return '/images/photo/{}/'.format(self.pk)


@python_2_unicode_compatible
class Album(md.Model):
    """Album to house images."""
    owner = md.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=md.CASCADE,
                              related_name='albums',
                              null=True)
    cover = md.ForeignKey('Photo', on_delete=md.CASCADE,
                          related_name='covered_albums', null=True,
                          default=None)
    title = md.CharField(default='', max_length=255)
    description = md.TextField(default='')
    date_uploaded = md.DateTimeField(auto_now_add=True)
    date_modified = md.DateTimeField(auto_now=True)
    date_published = md.DateTimeField(auto_now_add=True)
    published = md.CharField(max_length=7, choices=PUB_CHOICE,
                                 default='Private')


    def __str__(self):
        return self.title
