from django import forms
from forum.models import Discussion, Post, Section


class SectionModelForm(forms.ModelForm):

    class Meta:
        model = Section
        fields = ['name', 'description', 'logo']
        labels = {
            'name': 'Nome',
            'description': 'Descrizione',
            'logo': 'Immagine di copertina'
        }


class DiscussionModelForm(forms.ModelForm):
    """
    A form class for new discussions.

    Title and content are required.
    """

    content = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'A cosa stai pensando?'}),
        max_length=400,
        label='Primo Messaggio'
    )

    class Meta:
        model = Discussion
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Titolo della discussione'})
        }
        labels = {
            'title': 'Titolo'
        }


class PostModelForm(forms.ModelForm):
    """
    A form class for new post.

    Content is required.
    """

    class Meta:
        model = Post
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'placeholder': 'Rispondi...', 'rows': 5, 'id': 'content', 'onkeyup': 'reply()'})
        }
        labels = {
            'content': False
        }
