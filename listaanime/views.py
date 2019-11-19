from django.shortcuts import render
from .models import AnimeM
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .forms import AnimeForm
from django.template import loader
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status  
from .serializers import animeSerializer
from django.views.generic import TemplateView

def index(request):
    return render(request, 'listaanime/index.html')

def listaAnimes(request):
    lista_de_animes = AnimeM.objects.all()
    context = {'lista_de_animes': lista_de_animes}
    return render(request, 'listaanime/listaAnimes.html',context)

def login(request):
    return render(request, 'listaanime/login.html')

def detalleAnime(request,pk):
    anime = get_object_or_404(AnimeM,pk=pk)
    context = {'anime':anime}
    return render (request, 'listaanime/detalleAnime.html',context)   

def registroAnime(request):
    if request.method == 'POST':
        form = AnimeForm(request.POST,request.FILES)
        if form.is_valid():
            anime = form.save(commit=False)
            anime.save()
            return redirect('detalleAnime',pk=anime.pk)
    else:
        form = AnimeForm()
    context = {'form':form}
    return render(request, 'listaanime/registroAnime.html',context)

def anime_list(request):
    return render(request, 
    'listaanime/Anime.html', {}) 

def galeria_list(request):
    return render(request, 
    'listaanime/Galeria.html', {}) 

def manga_list(request):
    return render(request, 
    'listaanime/Manga.html', {})

  


class HomePageView(TemplateView):
    template_name = 'listaanime/home.html'    