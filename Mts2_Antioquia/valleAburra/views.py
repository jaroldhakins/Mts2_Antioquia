from django.shortcuts import render
from django.http import HttpResponse
from API.models import valle_aburra


def listarCiudad(request, barrio):
    valor = []
    mt2 = []
    ciudades = []
    todo = valle_aburra.objects.all()
    for i in todo:
        if i.barrio == barrio:
            mt2.append(i.mtsC)
            valor.append(i.price)
            ciudades.append(i.city)
    combinada = list(zip(ciudades, valor, mt2))
    return render(request, 'datos.html', {'combinadas': combinada})


def average(request):
    valor = []
    mt2 = []
    for i in valle_aburra.objects.all():
        if i.city == 'Medellin':
            mt2.append(i.mtsC)
            valor.append(i.price)
    metros = sum(mt2)
    totalPrecio = sum(valor)
    average_mts2 = totalPrecio / metros

    return render(request, 'valor_mt2.html', {'metros': f'Valor del Metro Cuadrado: {average_mts2:,.2f}'})


def comunas(request, ciudad):
    comunas = []
    for i in valle_aburra.objects.all():
        if i.city == ciudad:
            comunas.append(i.barrio)
    conjunto = set(comunas)
    return render(request, 'barrio.html', {'conjunto': conjunto})

def ciudades(request):
    ciudades = []
    for i in valle_aburra.objects.all():
        ciudades.append(i.city)
    conjunto_cities = set(ciudades)
    return render(request, 'ciudades.html', {'conjunto': conjunto_cities})
