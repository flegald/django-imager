"""Test Imager Profile."""
from django.test import TestCase
from .models import ImagerProfile
from django.contrib.auth.models import User


class TestProfile(TestCase):
    """Test ImagerProfile functionality."""

    def setUp(self):
        """Test new user creation."""
        self.test1 = User.objects.create_user('grumpy')
        self.test2 = User.objects.create_user('sneezy')
        self.test1.save()
        self.test2.save()


# ******
    def test_verify_save(self):
        """Test that IP are saving with User object."""
        self.assertEquals(len(ImagerProfile.objects.all()), 2)

# ******* index error
    def test_verify_profile(self):
        """Very profiles are saved to correct users."""
        self.assertEquals(ImagerProfile.objects.all()[0], self.test1.profile)

# *******
    def test_user_deletion(self):
        """Test when user is deleted so is profile."""
        self.assertEquals(len(ImagerProfile.objects.all()), 2)
        self.test1.delete()
        self.assertEquals(len(ImagerProfile.objects.all()), 1)

# ******
    def test_profile_deletion(self):
        """Test when profile is deleted user still exists."""
        self.assertEquals(len(User.objects.all()), 2)
        self.assertEquals(len(ImagerProfile.objects.all()), 2)
        self.test2.profile.delete()
        self.assertEquals(len(ImagerProfile.objects.all()), 1)
        self.assertEquals(len(User.objects.all()), 2)

    def test_profile_active(self):
        """Test profile is active."""
        self.assertEquals(self.test1.is_active, True)

    def test_friends(self):
        """Test friends realationship."""
        self.test1.profile.friends.add(self.test2)
        self.assertEquals(self.test1.profile.friends.all()[0], self.test2)
        self.assertEquals(self.test2.friend_of.all()[0], self.test1.profile)
