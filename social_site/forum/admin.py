from django.contrib import admin
from forum.models import Discussione, Post, Sezione

# Register your models here.
class DiscussioneModelAdmin(admin.ModelAdmin):
    """ Settings in order to improve management and visualization of Discussion's page in the admin's panel
        'autore_discussione' need '__username' in order to get the parameter as a string and execute the query """

    model = Discussione
    list_display = ['titolo', 'sezione_appartenenza', 'autore_discussione']
    search_fields = ['titolo', 'autore_discussione__username']
    list_filter = ['sezione_appartenenza', 'data_creazione']

class PostModelAdmin(admin.ModelAdmin):
    """ Settings in order to improve management and visualization of Post's page in the admin's panel """

    model = Post
    list_display = ['autore_post', 'discussione']
    search_fields = ['contenuto']
    list_filter = ['data_creazione', 'autore_post']

class SezioneModelAdmin(admin.ModelAdmin):
    """ Settings in order to improve management and visualization of Section's page in the admin's panel """

    model = Sezione
    list_display = ['nome_sezione', 'descrizione']

admin.site.register(Discussione, DiscussioneModelAdmin)
admin.site.register(Post, PostModelAdmin)
admin.site.register(Sezione, SezioneModelAdmin)
