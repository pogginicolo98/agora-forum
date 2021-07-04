from django import forms
from forum.models import Discussione, Post

class DiscussioneModelForm(forms.ModelForm):
    contenuto = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Di cosa vuoi parlarci?'}),
        max_length=400,
        label='Primo Messaggio'
    )
    class Meta:
        model = Discussione
        fields = ['titolo', 'contenuto']
        widgets = {
            'titolo': forms.TextInput(attrs={'placeholder': 'Titolo della discussione'})
        }

class PostModelForm(forms.ModelForm):

    class Meta:
        model = Post
        fields= ['contenuto']
        widgets = {
            'contenuto': forms.Textarea(attrs={'rows': 5})
        }
        labels = {
            'contenuto': 'Messaggio'
        }
