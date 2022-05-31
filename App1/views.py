from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from App1.models import datosfisicos, individuomedido, obscasuales
from App1.forms import BuscarIndividuosForm, fisform, indform, obsform
# Create your views here.

def index(request):
    individuos = individuomedido.objects.all()
    fisicos = datosfisicos.objects.all()
    observaciones = obscasuales.objects.all()
    template = loader.get_template('App1/lista_observaciones.html')
    context = {
        'individuos': individuos,
        'fisicos': fisicos,
        'observaciones': observaciones,
    }
    return HttpResponse(template.render(context, request))

def ind(request):
    if request.method=="POST":
        form = indform(request.POST)
        if form.is_valid():

            especie = form.cleaned_data['especie']
            nind = form.cleaned_data['nind']
            LargoTotal = form.cleaned_data['LargoTotal']
            peso = form.cleaned_data['peso']
            date = form.cleaned_data['date']
            km = form.cleaned_data['km']
            est = form.cleaned_data['est']            
            individuomedido(especie=especie,
                            nind=nind,
                            LargoTotal=LargoTotal,
                            peso=peso,
                            date=date,
                            km=km,
                            est=est).save()
            return HttpResponseRedirect("/")
    elif request.method=="GET":
       form =indform()
    else:
        return HttpResponseBadRequest("Error no conzco ese metodo para esta request")
    return render(request, 'App1/formind.html', {'form':form})

def fisico(request):
     if request.method == "POST":
        form = fisform(request.POST)
        if form.is_valid():

            date = form.cleaned_data['date']
            km = form.cleaned_data['km']
            est = form.cleaned_data['est']
            magnitud = form.cleaned_data['magnitud']
            medida = form.cleaned_data['medida']
            unidad = form.cleaned_data['unidad']
            datosfisicos(date=date,
                        km=km,
                        est=est,
                        magnitud=magnitud,
                        medida=medida,
                        unidad=unidad).save()
            return HttpResponseRedirect("/")
     elif request.method == "GET":
        form = fisform()
     else:
        return HttpResponseBadRequest("Error no conzco ese metodo para esta request")

     return render(request, 'App1/formfis.html', {'form': form})

def observ(request):
     if request.method == "POST":
        form = obsform(request.POST)
        if form.is_valid():

            especie = form.cleaned_data['especie']
            nind = form.cleaned_data['nind']
            date = form.cleaned_data['date']
            obs = form.cleaned_data['obs']
            obscasuales(date=date,
                        especie=especie,
                        nind=nind,
                        obs=obs).save()
            return HttpResponseRedirect("/")
     elif request.method == "GET":
        form = obsform()
     else:
        return HttpResponseBadRequest("Error no conzco ese metodo para esta request")

     return render(request, 'App1/formobs.html', {'form': form})

def buscar(request):
    if request.method == "GET":
        formbus = BuscarIndividuosForm()
        return render(request, 'App1/formbus.html', {"formbus": formbus})

    elif request.method == "POST":
        formbus = BuscarIndividuosForm(request.POST)
        if formbus.is_valid():
            palabra_a_buscar = formbus.cleaned_data['palabra_a_buscar']
            individuos = individuomedido.objects.filter(especie__icontains=palabra_a_buscar)
            fisicos = datosfisicos.objects.filter(magnitud__icontains=palabra_a_buscar)
            observaciones = obscasuales.objects.filter(especie__icontains=palabra_a_buscar)

        return  render(request, 'App1/lista_observaciones.html',
            {"individuos": individuos},
            {"fisicos": fisicos}, 
            {"observaciones": observaciones})



def borrar(request, identificador):
    if request.method == "GET":
        individuos = individuomedido.objects.filter(id=int(identificador)).first()
        fisicos = datosfisicos.objects.filter(id=int(identificador)).first()
        observaciones = obscasuales.objects.filter(id=int(identificador)).first()
        if individuos:
            individuos.delete()
        elif fisicos:
            fisicos.delete()
        elif observaciones:
            observaciones.delete()

        return HttpResponseRedirect("/")
    else:
        return HttpResponseBadRequest("Error no conzco ese metodo para esta request")
