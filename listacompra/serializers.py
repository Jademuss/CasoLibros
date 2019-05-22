from rest_framework import serializers
from .models import ProductosM



class productoSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductosM  
        fields = '__all__'