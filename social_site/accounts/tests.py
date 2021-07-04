from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus
from accounts.views import registrazione_view

# Create your tests here.
class Registrazione_view_Tests(TestCase):
    """ (view) registrazione_view's Tests class """

    def test_registrazione_view_url_by_name(self):
        url = reverse('registration_view')
        response = self.client.get(url)
        self.assertEquals(response.status_code, HTTPStatus.OK)
