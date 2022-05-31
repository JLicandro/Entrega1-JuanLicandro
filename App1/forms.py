from unittest.util import _MAX_LENGTH
from django import forms

class BuscarIndividuosForm(forms.Form):
    palabra_a_buscar= forms.CharField(label="Buscar")

class indform(forms.Form):
    especie = forms.CharField(label="Nombre de la especie", max_length=100) #Nombre de la especie
    nind = forms.IntegerField(label="Número de observaciones") #Número de individuo
    LargoTotal = forms.FloatField(label="Largo total",
        widget=forms.NumberInput(attrs={'placeholder': "15.5 mm"}))
    Peso= forms.FloatField(label="Peso húmedo de el/los individuos",
        widget=forms.NumberInput(attrs={'placeholder': "1.5 g"})) 
    date= forms.DateField(label="Fecha de muestreo", input_formats=["%d/%m/%Y"],
        widget = forms.TextInput(attrs={'placeholder': '30/12/1995'})) #Fecha de muestreo
    km= forms.IntegerField(label="Kilómetro de muestreo") #Kilómetro donde fue muestreado el individuo
    est= forms.IntegerField(label="Estación de muestreo") #Estación donde el individuo fue muestreado dentro del kilómetro anterior
    
class fisform(forms.Form):
    date= forms.DateField(label="Fecha de muestreo", input_formats=["%d/%m/%Y"],
        widget = forms.TextInput(attrs={'placeholder': '30/12/1995'})) #Fecha de muestreo
    km= forms.IntegerField(label="Kilómetro de muestreo") #Kilómetro donde fue muestreado el individuo
    est= forms.IntegerField(label="Estación de muestreo") #Estación donde el individuo fue muestreado dentro del kilómetro anterior    
    magnitud= forms.CharField(label="Magnitud", max_length=100) #Nombre de la magnitud
    medida= forms.FloatField(label="Medida",
        widget=forms.NumberInput(attrs={'placeholder': "10.5"})) #Medida de la magnitud en cuestión
    unidad= forms.CharField(label="Unidad de medida", max_length=10,
        widget=forms.NumberInput(attrs={'placeholder': "°C"}))

class obsform(forms.Form):
    especie = forms.CharField(label="Nombre de la especie", max_length=100) #Nombre de la especie
    nind = forms.IntegerField(label="Número de observaciones") #Número de individuo
    date= forms.DateField(label="Fecha de muestreo", input_formats=["%d/%m/%Y"],
        widget = forms.TextInput(attrs={'placeholder': '30/12/1995'})) #Fecha de muestreo
    obs= forms.CharField(label="Observaciones", max_length=150) #Descripción de la especie, ubicación y comportamiento

