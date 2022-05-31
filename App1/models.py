from django.db import models

# Create your models here.
class individuomedido(models.Model):
    especie = models.CharField(max_length=100) #Nombre de la especie
    nind = models.IntegerField() #Número de individuo
    LargoTotal = models.FloatField(default=0.0)
    peso= models.FloatField(default=0.0) 
    date= models.DateField() #Fecha de muestreo
    km= models.IntegerField() #Kilómetro donde fue muestreado el individuo
    est= models.IntegerField() #Estación donde el individuo fue muestreado dentro del kilómetro anterior

class datosfisicos(models.Model):
    date= models.DateField() #Fecha de muestreo
    km= models.IntegerField() #Kilómetro donde fue muestreado el individuo
    est= models.IntegerField() #Estación donde el individuo fue muestreado dentro del kilómetro anterior
    magnitud= models.CharField(max_length=100) #Nombre de la magnitud
    medida= models.FloatField(default=0.0) #Medida de la magnitud en cuestión
    unidad= models.CharField(max_length=10) #unidad de medida de la magnitud agregada

class obscasuales(models.Model):
    especie = models.CharField(max_length=100) #Nombre de la especie
    nind = models.IntegerField() #Número de individuo
    date= models.DateField() #Fecha de muestreo
    obs= models.CharField(max_length=150) #Descripción de la especie, ubicación y comportamiento
