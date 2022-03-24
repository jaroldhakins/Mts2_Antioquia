from django.urls import path
from .views import ApiListView, ApiDetailView

urlpatterns = [
    path('listado/', ApiListView.as_view(), name='listado'),

]
