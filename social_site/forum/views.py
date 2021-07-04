from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.views.generic.edit import CreateView, DeleteView
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.urls import reverse
from forum.forms import DiscussioneModelForm, PostModelForm
from forum.mixins import StaffMixin
from forum.models import Discussione, Post, Sezione

# Create your views here.
class CreaSezione(StaffMixin,CreateView):
    model = Sezione
    fields = '__all__'
    template_name = 'forum/crea_sezione.html'
    success_url = '/'

def visualizza_sezione(request, pk):
    sezione = get_object_or_404(Sezione, pk=pk)
    discussioni_sezione = Discussione.objects.filter(
        sezione_appartenenza=sezione
    ).order_by('-data_creazione')
    context = {
        'sezione': sezione,
        'discussioni': discussioni_sezione
    }
    return render(request, 'forum/singola_sezione.html', context)

@login_required
def crea_discussione(request, pk):
    sezione = get_object_or_404(Sezione, pk=pk)
    if request.method == 'POST':
        form = DiscussioneModelForm(request.POST)
        if form.is_valid():
            discussione = form.save(commit=False)
            discussione.sezione_appartenenza = sezione
            discussione.autore_discussione = request.user
            discussione.save()
            primo_post = Post.objects.create(
                discussione=discussione,
                autore_post=request.user,
                contenuto=form.cleaned_data['contenuto']
            )
            return HttpResponseRedirect(discussione.get_absolute_url())
    else:
        form = DiscussioneModelForm()
    context = {
        'form': form,
        'sezione': sezione
    }
    return render(request, 'forum/crea_discussione.html', context)

def visualizza_discussione(request, pk):
    discussione = get_object_or_404(Discussione, pk=pk)
    posts_discussione = Post.objects.filter(discussione=discussione)
    form_risposta = PostModelForm()
    paginator = Paginator(posts_discussione, 5)
    page_number = request.GET.get('pagina')
    page_obj = paginator.get_page(page_number)
    context = {
        'discussione': discussione,
        'form_risposta': form_risposta,
        'page_obj': page_obj
    }
    return render(request, 'forum/singola_discussione.html', context)

@login_required
def aggiungi_risposta(request, pk):
    discussione = get_object_or_404(Discussione, pk=pk)
    if request.method == 'POST':
        form = PostModelForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.instance.discussione = discussione
            form.instance.autore_post = request.user
            form.save()
            url_discussione = reverse('visualizza_discussione', kwargs={'pk': pk})
            pagine_in_discussione = discussione.get_n_pages()
            if pagine_in_discussione > 1:
                success_url = f"{url_discussione}?pagina={pagine_in_discussione}"
                return HttpResponseRedirect(success_url)
            else:
                return HttpResponseRedirect(url_discussione)
    else:
        return HttpResponseBadRequest

class CancellaPost(DeleteView):
    model = Post
    success_url = '/'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(autore_post=self.request.user)
