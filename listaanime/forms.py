from django import forms
from .models import AnimeM
""""from django.contrib.auth.models import User"""

class AnimeForm(forms.ModelForm):
    
    class Meta:
        model = AnimeM
        fields = ['nombre','image_anime','descripcion' ]
        

