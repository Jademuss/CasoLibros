from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),    
    path('index', views.index, name='index'),
    path('index/anime_list/', views.anime_list, name='anime_list'),
    path('index/galeria_list', views.galeria_list, name='galeria_list'),
    path('index/manga_list', views.manga_list, name='manga_list'),
    path('index/registroAnime/', views.registroAnime, name='registroAnime'),
    path('index/detalleAnime/<int:pk>/', views.detalleAnime, name='detalleAnime'),     
    path('index/listaAnimes/', views.listaAnimes, name='listaAnimes')  

]	