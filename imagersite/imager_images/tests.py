from django.db.models.fields.files import ImageFieldFile
from django.test import TestCase, override_settings
from .models import Photo, Album, PUB_CHOICE
from django.conf import settings

import factory
import random

TEMP_MEDIA_ROOT = '/tmp/media/'


class UserFactory(factory.django.DjangoModelFactory):
    """Create Users."""

    class Meta:

        model = settings.AUTH_USER_MODEL
        django_get_or_create = ('username',)

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.Faker('email')
    username = factory.LazyAttribute(
        lambda obj: ''.join((obj.first_name, obj.last_name)))
    password = factory.PostGenerationMethodCall('set_password', 'secret')


class PhotoFactory(factory.django.DjangoModelFactory):
    """Create Photos."""

    class Meta:
        model = Photo

    title = factory.Faker('sentence')
    description = factory.Faker('sentence')
    published = random.choice(PUB_CHOICE[0])
    owner = factory.SubFactory(UserFactory, username='Gma666')
    img_file = factory.django.ImageField()


class AlbumFactory(factory.django.DjangoModelFactory):
    """Create Albums."""

    class Meta:
        model = Album

    title = factory.Faker('sentence')
    description = factory.Faker('sentence')
    published = random.choice(PUB_CHOICE)
    owner = factory.SubFactory(UserFactory, username='Gma666')


class BasicTest(object):
    """Test that basic class created properly."""

    def test_exist(self):
        """Test existence."""
        self.assertTrue(self.instance)

    def test_title(self):
        """Test title generated."""
        self.assertTrue(self.instance.title)

    def test_description(self):
        """Test description generated."""
        self.assertTrue(self.instance.description)

    def test_published(self):
        """Test published generated."""
        self.assertTrue(self.instance.published)

    def test_owner(self):
        """Test owner generated."""
        self.assertTrue(self.instance.owner)

    def test_date_uploaded(self):
        """Test date_uploaded generated."""
        self.assertTrue(self.instance.date_uploaded)

    def test_date_modified(self):
        """Test date_modified generated."""
        self.assertTrue(self.instance.date_modified)

    def test_date_published(self):
        """Test date_published generated."""
        self.assertTrue(self.instance.date_published)


@override_settings(MEDIA_ROOT=TEMP_MEDIA_ROOT)
class Photo(TestCase, BasicTest):
    """Test photo instance."""

    def setUp(self):
        """Initiate Photo instance."""
        self.instance = PhotoFactory.create()

    def test_empty_album(self):
        """Test Photo has no albums."""
        self.assertFalse(self.instance.albums.count())

    def test_img_file_exists(self):
        """Test img_file exists."""
        self.assertTrue(self.instance.img_file)

    def test_img_file_type(self):
        """Test img file type correct."""
        self.assertIsInstance(self.instance.img_file, ImageFieldFile)


@override_settings(MEDIA_ROOT=TEMP_MEDIA_ROOT)
class Album(TestCase, BasicTest):
    """Test Album instance."""

    def setUp(self):
        """Initiate Album."""
        self.instance = AlbumFactory.create()

    def test_empty_album(self):
        """Test album has no photos."""
        self.assertFalse(self.instance.photos.count())


@override_settings(MEDIA_ROOT=TEMP_MEDIA_ROOT)
class PhotosAlbum(TestCase):
    """A Lot of photos, one album."""

    def setUp(self):
        """Create photos and albums."""
        self.photos = PhotoFactory.create_batch(50)
        self.album = AlbumFactory.create()
        self.album2 = AlbumFactory.create()

        for photo in self.photos:
            self.album.photos.add(photo)

    def test_album_size(self):
        """Test photos in album."""
        self.assertEquals(self.album.photos.count(), 50)

    def test_owner_match(self):
        """Test owner is correct."""
        for photo in self.photos:
            self.assertEquals(photo.owner, self.album.owner)

    def test_photos_in_multiple_albums(self):
        """Test photos are in multiple albums."""
        for photo in self.photos:
            self.album2.photos.add(photo)
        for photo in self.photos:
            self.assertIn(photo, self.album.photos.all())
            self.assertIn(photo, self.album2.photos.all())



