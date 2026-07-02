from django.urls import path
from .views import lista_tarefas

urlpatterns = [
    path('', lista_tarefas, name='lista_tarefas'),
]