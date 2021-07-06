from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic.list import ListView
from forum.models import Discussion, Section, Post


class Homepage(ListView):
    """ ListView that shows a list of all sections active in the forum """

    queryset = Section.objects.all().order_by('pk')
    template_name = 'core/homepage_it.html'
    context_object_name = 'sections'


class UsersList(LoginRequiredMixin, ListView):
    """ ListView that shows a list of all users signed up """

    model = User
    template_name = 'core/users_it.html'
    context_object_name = 'users'


def user_profile_view(request, username):
    # Get the user corresponding the username passed through the url user/'username' and show the profile page

    user = get_object_or_404(User, username=username)
    user_discussions = Discussion.objects.filter(discussion_author=user).order_by('-pk')
    context = {
        'user': user,
        'user_discussions': user_discussions
    }
    return render(request, "core/user_profile_it.html", context)


def search_bar(request):
    # Search in discussions, posts and users for the keyword written in the search bar

    if 'search' in request.GET:
        # URL contains 'search'
        querystring = request.GET.get('search')
        if len(querystring) == 0:
            return redirect('/search/')
        discussions = Discussion.objects.filter(title__icontains=querystring)
        print(discussions)
        posts = Post.objects.filter(content__icontains=querystring)
        users = User.objects.filter(username__icontains=querystring)
        print(users)
        context = {
            'discussions': discussions,
            'posts': posts,
            'users': users
        }
        return render(request, 'core/search_it.html', context)
    else:
        return render(request, 'core/search_it.html')
