"""Imager Profile."""
from django.db import models as md
from django.utils.encoding import python_2_unicode_compatible
from django.conf import settings
from django.contrib.auth.models import User


PHOTOGRAPHY_TYPES = [
    ('portrait', 'Portrait'),
    ('landscape', 'Landscape'),
    ('nature', 'Nature'),
    ('family', 'Family'),
    ('travel', 'Travel'),
    ('art', 'Art'),
    ('food', 'Food'),
]


class ActiveUserManager(md.Manager):
    """Show active users."""

    def get_queryset(self):
        qs = super(ActiveUserManager, self).get_queryset()
        return qs.filter(user__is_active__exact=True)


@python_2_unicode_compatible
class ImagerProfile(md.Model):
    """An extension of Djangos User Class to build Imager Profile."""

    user = md.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=md.CASCADE,
                                related_name='profile',
                                null=False)
    location = md.CharField(default='', max_length=255, null=True, blank=True)
    bio = md.TextField(default='', null=True, blank=True)
    camera = md.TextField(default='', max_length=255, null=True, blank=True)
    friends = md.ManyToManyField(User,
                            related_name='friend_of')
    photography_type = md.CharField(max_length=255,
                                    choices=PHOTOGRAPHY_TYPES,
                                    default='art')

    def __str__(self):
        """Return string of username."""
        return self.user.username

    objects = md.Manager()
    active = ActiveUserManager()

    @property
    def is_active(self):
        """Return True if user has active profile."""
        return self.user.is_active
