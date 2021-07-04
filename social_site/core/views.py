from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic.list import ListView
from forum.models import Discussione, Sezione, Post

# Create your views here.
class HomeView(ListView):
    queryset = Sezione.objects.all()
    template_name = 'core/homepage.html'
    context_object_name = 'lista_sezioni'

class UsersList(LoginRequiredMixin, ListView):
    """ ListView showing a list of all users registered """

    model = User
    template_name = 'core/users.html'

def user_profile_view(request, username):
    # Getting the user corresponding the username passed through the url user/'username' and show the profile page
    user = get_object_or_404(User, username=username)
    discussioni_utente = Discussione.objects.filter(autore_discussione=user).order_by('-pk')
    context = {
        'user': user,
        'discussioni_utente': discussioni_utente
    }
    return render(request, "core/user_profile.html", context)

def cerca(request):
    if 'q' in request.GET:
        querystring = request.GET.get('q')
        if len(querystring) == 0:
            return redirect('/cerca/')
        discussioni = Discussione.objects.filter(titolo__icontains=querystring)
        posts = Post.objects.filter(contenuto__icontains=querystring)
        users = User.objects.filter(username__icontains=querystring)
        context = {
            'discussioni': discussioni,
            'posts': posts,
            'users': users
        }
        return render(request, 'core/cerca.html', context)
    else:
        return render(request, 'core/cerca.html')
