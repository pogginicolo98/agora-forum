from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    """
    A form class for sign up new users.

    Username, password and email are required.
    password1 and password2 must match.
    """

    # Overriding the User email field
    email = forms.CharField(max_length=40, required=True, widget=forms.EmailInput())

    class Meta:
        # Setting the model class and parameters in order to generate the relative forms
        model = User
        fields = ['username', 'email', 'password1', 'password2']
