from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from accounts.forms import FormRegistrazione

# Create your views here.
def registrazione_view(request):
    # View function for the user registration

    if request.method == 'POST':
        # Binded session, forms validation
        form = FormRegistrazione(request.POST)
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
        # New session, forms empty
        form = FormRegistrazione()

    context = {'form': form}
    return render(request, 'accounts/registrazione.html', context)
