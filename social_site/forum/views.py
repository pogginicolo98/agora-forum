from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.views.generic.edit import CreateView, DeleteView
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.urls import reverse
from forum.forms import DiscussionModelForm, PostModelForm, SectionModelForm
from forum.mixins import StaffMixin
from forum.models import Discussion, Post, Section


class NewSection(StaffMixin, CreateView):
    model = Section
    form_class = SectionModelForm
    template_name = 'forum/new_section_it.html'
    success_url = '/'


class DeleteSection(StaffMixin, DeleteView):
    model = Section
    success_url = '/'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset


class DeletePost(DeleteView):
    model = Post
    success_url = '/'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(post_author=self.request.user)


def section_view(request, pk):
    section = get_object_or_404(Section, pk=pk)
    discussions = Discussion.objects.filter(
        discussion_section=section
    ).order_by('-creation_date')
    context = {
        'section': section,
        'discussions': discussions
    }
    return render(request, 'forum/section_it.html', context)


@login_required
def new_discussion(request, pk):
    discussion_section = get_object_or_404(Section, pk=pk)
    if request.method == 'POST':
        form = DiscussionModelForm(request.POST)
        if form.is_valid():
            discussion = form.save(commit=False)
            discussion.discussion_section = discussion_section
            discussion.discussion_author = request.user
            discussion.save()
            Post.objects.create(
                post_discussion=discussion,
                post_author=request.user,
                content=form.cleaned_data['content']
            )
            return HttpResponseRedirect(discussion.get_absolute_url())
    else:
        form = DiscussionModelForm()
    context = {
        'form': form,
        'discussion_section': discussion_section
    }
    return render(request, 'forum/new_discussion_it.html', context)


def discussion_view(request, pk):
    discussion = get_object_or_404(Discussion, pk=pk)
    discussion_posts = Post.objects.filter(post_discussion=discussion)
    reply_form = PostModelForm()
    paginator = Paginator(discussion_posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'discussion': discussion,
        'reply_form': reply_form,
        'page_obj': page_obj
    }
    return render(request, 'forum/discussion_it.html', context)


@login_required
def reply(request, pk):
    discussion = get_object_or_404(Discussion, pk=pk)
    if request.method == 'POST':
        form = PostModelForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.instance.post_discussion = discussion
            form.instance.post_author = request.user
            form.save()
    else:
        return HttpResponseBadRequest
    url_discussione = reverse('discussion_view', kwargs={'pk': pk})
    discussion_pages = discussion.get_n_pages()
    if discussion_pages > 1:
        success_url = f"{url_discussione}?page={discussion_pages}"
        return HttpResponseRedirect(success_url)
    else:
        return HttpResponseRedirect(url_discussione)
