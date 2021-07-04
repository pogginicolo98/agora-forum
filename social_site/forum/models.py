from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from math import ceil

# Create your models here.
class Sezione(models.Model):
    """ The 'Sections' divide the site in discussion categories.
        Each 'Section' contains several 'Discussions'
        Only site administrators can create 'Sections' """

    nome_sezione = models.CharField(max_length=80)
    descrizione = models.CharField(max_length=150, blank=True, null=True)
    logo_sezione = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.nome_sezione

    def get_absolute_url(self):
        return reverse('sezione_view', kwargs={'pk': self.pk})

    def get_last_discussions(self):
        return Discussione.objects.filter(sezione_appartenenza=self).order_by('-data_creazione')[:2]

    def get_number_of_posts_in_section(self):
        return Post.objects.filter(discussione__sezione_appartenenza=self).count()

    class Meta:
        verbose_name = 'Sezione'
        verbose_name_plural = 'Sezioni'
        ordering = ['nome_sezione']

class Discussione(models.Model):
    """ 'Discussions' are created by 'Users'.
        Each 'Discussion' belongs to a 'Section'
        Each 'Discussion' cointain several 'Posts' """

    titolo = models.CharField(max_length=120)
    data_creazione = models.DateTimeField(auto_now_add=True)
    autore_discussione = models.ForeignKey(User, on_delete=models.CASCADE, related_name='discussioni')
    sezione_appartenenza = models.ForeignKey(Sezione, on_delete=models.CASCADE)

    def __str__(self):
        return self.titolo

    def get_absolute_url(self):
        return reverse('visualizza_discussione', kwargs={'pk': self.pk})

    def get_n_pages(self):
        posts_discussione = self.post_set.count()
        n_pagine = ceil(posts_discussione / 5)
        return n_pagine

    class Meta:
        verbose_name = 'Discussione'
        verbose_name_plural = 'Discussioni'
        ordering = ['data_creazione']

class Post(models.Model):
    """ 'Posts' are created by 'Users'
        Each 'Post' belogns to a 'Discussion' """

    autore_post = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    contenuto = models.TextField()
    data_creazione = models.DateTimeField(auto_now_add=True)
    discussione = models.ForeignKey(Discussione, on_delete=models.CASCADE)

    def __str__(self):
        return self.autore_post.username

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['data_creazione']
