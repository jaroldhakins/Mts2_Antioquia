from django.shortcuts import render
from django.http import HttpResponse
from predios.models import valle_aburra

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
    return HttpResponse(f'Valor del Metro Cuadrado: {average_mts2:,.2f}')
