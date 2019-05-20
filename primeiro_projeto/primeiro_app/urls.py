from django.contrib import admin
from django.urls import path
from primeiro_app import views

urlpatterns = [
   path('', views.home, name='home'),
    path('alunos/', views.alunos, name='alunos'),
    path('alunos/<int:id>/', views.detalhes, name='alunos-detalhes'),
    path('servidores/', views.servidores, name='servidores'),
    path('servidores/<int:id>/', views.servidor_detalhes, name='servidores-detalhes')
]