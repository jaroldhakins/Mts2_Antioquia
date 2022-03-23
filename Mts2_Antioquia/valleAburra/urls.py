from django.urls import path

from valleAburra.views import average

urlpatterns = [
    path('valormt2', average),
]
