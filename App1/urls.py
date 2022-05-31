from django.contrib import admin
from django.urls import path
from App1 import views

urlpatterns = [
    path('', views.index, name="index"),
    path('ind/', views.ind, name="ind"),
    path('fis/', views.fisico, name="fis"),
    path('obs/', views.observ, name='obs'),
    path('buscar/', views.buscar, name='buscar'),
    path('borrar/<identificador>', views.borrar, name="borrar")    
]
