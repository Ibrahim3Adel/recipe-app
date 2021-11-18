from unittest.case import _AssertRaisesContext
from django.test import TestCase

from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'hemaplaypopo@gmail.com'
        password = 'testpass1234'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

    def test_new_user_email_normailzed(self):
        """Test the email for a new is normalized"""
        email = 'hemaplaypopo@gmail.com'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123s')

    def test_create_new_superuser(self):
        user = get_user_model().objects.create_superuser(
            'hemaplaypopo@gmail.com',
            'test123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
