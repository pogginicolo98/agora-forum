from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus


class SignUpViewTests(TestCase):
    """
    (view) Signup_view tests.

    A class that perform the following tests:
    1 - Url by name
    """

    def test_signup_view_url_by_name(self):
        url = reverse('signup_view')
        response = self.client.get(url)
        self.assertEquals(response.status_code, HTTPStatus.OK)
