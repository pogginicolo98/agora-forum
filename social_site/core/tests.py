from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus
from django.contrib.auth.models import User


class HomepageTests(TestCase):
    """
    (view) Homepage tests.

    A class that perform the following tests:
    1 - Url by name
    """

    def test_homepage_url_by_name(self):
        url = reverse('homepage')
        response = self.client.get(url)
        self.assertEquals(response.status_code, HTTPStatus.OK)


class UserListTests(TestCase):
    """
    (view) UserList tests.

    A class that perform the following tests:
    1 - Url by name
    """

    def test_UserList_url_by_name(self):
        url = reverse('users_list')
        response = self.client.get(url)
        self.assertEquals(response.status_code, HTTPStatus.OK)


class UserProfileViewTests(TestCase):
    """
    (view) user_profile_view tests.

    A class that perform the following tests:
    1 - Url by name
    """

    def setUp(self):
        User.objects.create_user(
            username="Mario",
            password="Password123!",
            email="usermario@mail.com"
        )

    def test_user_profile_view_url_by_name(self):
        url = reverse('user_profile', kwargs={'username': "Mario"})
        response = self.client.get(url)
        self.assertEquals(response.status_code, HTTPStatus.OK)
