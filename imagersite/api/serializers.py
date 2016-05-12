"""Serializers for imager API."""
from rest_framework import serializers
from imager_images.models import Photo, Album


class PhotoSerializer(serializers.HyperlinkedModelSerializer):
    """API serializer for the Photos."""

    owner = serializers.ReadOnlyField(source='owner.username')
    img_file = serializers.FileField(use_url=True)

    class Meta:
        """Meta."""

        model = Photo
        fields = ['owner', 'img_file', 'title', 'description',
                  'published', 'date_uploaded', 'date_published',
                  'date_modified']


class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    """API serializer for the Albums."""

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        """Meta."""

        model = Album
        fields = ['owner', 'title', 'description',
                  'published', 'date_uploaded', 'date_published',
                  'date_modified']

