from django.shortcuts import render
from django.views import View
from .models import valle_aburra
from django.http import JsonResponse


class ApiListView(View):
    def get(self, request):
        lista = valle_aburra.objects.all()
        return JsonResponse(list(lista.values()), safe=False)
    def post(self, request):
        pass
    def put(self, request):
        pass
    def delete(self, request):
        pass


class ApiDetailView(View):
    def get(self, request, pk):
        lista = valle_aburra.objects.get(pk=pk)
        return JsonResponse(lista, False)
    def post(self, request):
        pass
    def put(self, request):
        pass
    def delete(self, request):
        pass
