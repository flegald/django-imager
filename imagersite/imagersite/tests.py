"""Tests for login/logout/registration/urls"""
from __future__ import unicode_literals
from django.core import mail
from django.test import Client, TestCase
from django.contrib.auth.models import AnonymousUser, User
from django.contrib.auth.forms import AuthenticationForm
from registration.forms import RegistrationForm
import re

HOME = '/'
REGISTER = '/accounts/register/'
LOGIN = '/accounts/login'
LOGOUT = 'accounts/logout'

BAD_LOGIN = {'username': 'Fake', 'password': 'fakepw'}
GOOD_LOGIN = {'username': 'Real', 'password': 'realpw'}

BAD_REGISTER = {'username': 'Fake',
                'email': 'fake@fake.com',
                'password1': 'fakepw1',
                'password2': 'fakepw2'}

GOOD_REGISTER = {'username': 'Real',
                'email': 'real@real.com',
                'password1': 'realpw',
                'password2': 'realpw'}

REG_LINK = r'/accounts/activate/.*/'


class Unauthenticated(TestCase):
    """Testing with unathenticated user."""

    def setUp(self):
        """Set up unauthenticated user."""
        client = Client()
        self.home_response = client.get(HOME)
        self.register_response = client.get(REGISTER)
        self.bad_register = client.post(REGISTER, BAD_REGISTER)
        self.login_repsonse = client.get(LOGIN)
        self.bad_login_post = client.post(LOGIN, BAD_LOGIN)
        self.logout = client.get(LOGOUT)

    def test_home_200(self):
        """Check homepage shows."""
        self.assertEquals(self.home_response.status_code, 200)

    def test_register_200(self):
        """Check register shows."""
        self.assertEquals(self.register_response.status_code, 200)


class Registration(TestCase):
    """Test Registration."""

    def setUp(self):
        """Set up registration client test."""
        self.client = Client()
        self.good_register = self.client.post(REGISTER, GOOD_REGISTER, follow=True)

        try:
            self.email = mail.outbox[0]
        except IndexError:
            self.email = None

    def tearDown(self):
        """Cleanse the testing field."""
        for user in User.objects.all():
            user.delete()

    def test_user_is_inactive(self):
        """Check user in db is inactive."""
        self.assertIsInstance(User.objects.first(), None)

    def test_good_registration(self):
        """Test registration w/ correct info works."""
        self.assertEquals(self.good_register.status_code, 200)

    def test_registration_redirect(self):
        """Check after good registration is redirect to home."""
        self.assertIn(('/accounts/register/complete/', 302),
                      self.good_register.redirect_chain)

    def test_email_sent(self):
        """Check that registration email was sent."""
        self.assertTrue(self.email)


class Authenticated(TestCase):
    """Test with authenticated user."""

    def setUp(self):
        """Set up authenticated user case."""
        self.client = Client()
        self.client.post(REGISTER, GOOD_REGISTER, follow=True)

        try:
            email = mail.outbox[0]
            path = re.search(REG_LINK, email.body.group())
            self.client.get(path, follow=True)
        except IndexError:
            email = None

        self.user = User.objects.first()

        login_info = {'username': GOOD_REGISTER['username'],
                    'password': GOOD_REGISTER['password1']}

        self.login = self.client.post(LOGIN, login_info, follow=True)

    def tearDown(self):
        """Cleanse the testing field."""
        self.user.delete()

    def test_user_in_db(self):
        """Test for one user in db."""
        self.assertEquals(User.objects.count(), 1)
        self.assertEquals(User.objects.first(), self.user)

    def test_user_is_active(self):
        """Check that user is active."""
        self.asssertTrue(self.user.is_active())

    def test_re_register(self):
        """Make sure user can not register twice."""
        resp = self.client.post(REGISTER, GOOD_REGISTER)
        self.assertEquals(resp.status_code, 200)
        self.assertIn(b'A User with that username already exists.', resp.content)

    def test_good_login(self):
        """Test login works with correct info."""
        self.assertEquals(self.login.status_code, 200)

    def test_fir_request_dot_user(self):
        """Check for request.user on authntication."""
        for item in self.login.context[0]:
            user = item.get('user')
            if user:
                break
        self.assertIsInstance(user, User)


