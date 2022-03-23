from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')


"""def barrios(request, ciudad):
    if ciudad == 'Medellin':
    return render(request, 'barrio.html')
"""