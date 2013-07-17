from django.test import TestCase
from django.core.urlresolvers import reverse


class AccountsTests(TestCase):
    """
    Tests view behavior and urls
    """
    fixtures = ['TestDump.json']

    def test_login_redirect(self):
        """
        Redirect to profile page on login
        """
        response = self.client.post(reverse('accounts:login'), {
            'username': 'example_user_1',
            'password': 'test',
        })
        self.assertEqual(response.status_code, 302)

        msg = 'User was not redirected to profile page after login'
        location = response._headers['location'][1]
        self.assertTrue(reverse('accounts:profile') in location, msg=msg)

    def test_password_change(self):
        """
        Allow users to change their password
        """
        logged_in = self.client.login(
            username='example_user_1', password='test')
        assert logged_in
        response = self.client.post(reverse('accounts:pw_change'))
        self.assertEqual(response.status_code, 200)

        response = self.client.post(reverse('accounts:pw_change'), {
            'old_password': 'asdf',
            'new_password1': 'asdf',
            'new_password2': 'asdf',
        })
        self.assertEqual(response.status_code, 200)

        response = self.client.post(reverse('accounts:pw_change'), {
            'old_password': 'test',
            'new_password1': 'asdfasdf',
            'new_password2': 'asdfasdf',
        })
        self.assertEqual(response.status_code, 302)

        msg = 'The user is being misdirected after a password change'
        location = response._headers['location'][1]
        self.assertTrue(
            reverse('accounts:pw_change_success') in location, msg=msg)

        response = self.client.post(reverse('accounts:pw_change'), {
            'old_password': 'asdfasdf',
            'new_password1': 'testtest',
            'new_password2': 'testtest',
        })
        self.assertEqual(response.status_code, 302)

    def test_password_length(self):
        """
        Enforce password length requirements
        """
        logged_in = self.client.login(
            username='example_user_1', password='test')
        assert logged_in
        response = self.client.post(reverse('accounts:pw_change'))
        self.assertEqual(response.status_code, 200)

        response = self.client.post(reverse('accounts:pw_change'), {
            'old_password': 'test',
            'new_password1': 'test2',
            'new_password2': 'test2',
        })
        msg = 'Password length requirements are not enforced'
        self.assertEqual(response.status_code, 200, msg=msg)

        response = self.client.post(reverse('accounts:pw_change'), {
            'old_password': 'test',
            'new_password1': 'testtest',
            'new_password2': 'testtest',
        })
        self.assertEqual(response.status_code, 302)

        msg = 'The user is being misdirected after a password change'
        location = response._headers['location'][1]
        self.assertTrue(
            reverse('accounts:pw_change_success') in location, msg=msg)
