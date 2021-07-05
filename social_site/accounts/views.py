from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from accounts.forms import SignUpForm


def signup_view(request):
    # Function for sign up new users

    if request.method == 'POST':
        # Bound session, compiled form
        form = SignUpForm(request.POST)
        if form.is_valid():
            # User registration
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            User.objects.create_user(
                username=username,
                password=password,
                email=email
            )
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect('/')
    else:
        # New session, empty form
        form = SignUpForm()

    context = {'form': form}
    return render(request, 'accounts/signup_it.html', context)
