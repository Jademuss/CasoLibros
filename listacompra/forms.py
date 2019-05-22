from django import forms
from .models import ProductosM
""""from django.contrib.auth.models import User"""

class ProductoForm(forms.ModelForm):
    
    class Meta:
        model = ProductosM
        fields = ['nombre','image_producto','precio','descripcion' ]
        

