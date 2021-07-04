from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus
from django.contrib.auth.models import User
from core.views import homepage, UsersList, user_profile_view

# Create your tests here.
class Homepage_Tests(TestCase):
    """ (view) homepage's Tests class """

    def test_homepage_url_by_name(self):
        url = reverse('homepage')
        response = self.client.get(url)
        self.assertEquals(response.status_code, HTTPStatus.OK)

class UserList_Tests(TestCase):
    """ (view) UserList's Tests class """

    def test_UserList_url_by_name(self):
        url = reverse('users')
        response = self.client.get(url)
        self.assertEquals(response.status_code, HTTPStatus.OK)

class User_profile_view_Tests(TestCase):
    """ (view) user_profile_view's Tests class """

    def setUp(self):
        User.objects.create_user(
            username="User_Mario",
            password="Asdqwe123$",
            email="usermario@mail.com"
        )

    def test_user_profile_view_url_by_name(self):
        url = reverse('user_profile', kwargs={'username': "User_Mario"})
        response = self.client.get(url)
        self.assertEquals(response.status_code, HTTPStatus.OK)
