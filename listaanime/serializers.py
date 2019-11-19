from rest_framework import serializers
from .models import AnimeM



class animeSerializer(serializers.ModelSerializer):

    class Meta:
        model = AnimeM  
        fields = '__all__'