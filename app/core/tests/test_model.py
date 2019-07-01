from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successfull(self):
        email = 'darshan@gmail.com'
        password = 'darshan31'
        user = get_user_model().objects.create_user(email=email,
                                                    password=password)
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        email = 'darshan@GMAIL.com'
        user = get_user_model().objects.create_user(email, 'darshan31')
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'darshan31')

    def test_create_new_super_user(self):
        user = get_user_model().objects.create_superuser('darshan@gmail.com',
                                                         'darshan31')
        self.assertTrue(user.is_staff)
        self.assertTrue((user.is_superuser))

    