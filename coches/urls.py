from django.urls import path
from . import views

urlpatterns = [
    path('scrapear-milanuncios/', views.scrapear_milanuncios, name='scrapear_coches'),
    path('', views.lista_coches, name='lista_coches'),
]




