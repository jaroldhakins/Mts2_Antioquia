from django.urls import path

from valleAburra.views import listarCiudad, average, comunas, ciudades

urlpatterns = [
    path('lotes_ciudad/<str:barrio>', listarCiudad),
    path('valormt2/', average),
    path('ciudad/<str:ciudad>', comunas),
    path('ciudades/', ciudades),
]
