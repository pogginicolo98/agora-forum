from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FormRegistrazione(UserCreationForm):
    """ A ModelForm for creating a new user.
        It has three fields: username (from the user model), password1, and password2.
        It verifies that password1 and password2 match """

    # Overriding the User's email field
    email = forms.CharField(max_length=30, required=True, widget=forms.EmailInput())

    class Meta:
        # Setting the model class and parameters in order to generate the forms
        model = User
        fields = ['username', 'email', 'password1', 'password2']
