from django.shortcuts import render, HttpResponse
from . models import Aluno, Servidor

def home(request):
    nome = 'João'
    return render(request, 'index.html', {'nome': nome})

def alunos(request):
   alunos = Aluno.objects.all()
   return render(request, 'alunos.html', {'alunos': alunos})

def detalhes(request, id):
   a_detalhe = Aluno.objects.get(id=id)
   return render(request, 'detalhes.html', {'detalhe': a_detalhe})

def servidores(request):
    servidores = Servidor.objects.all()
    return render(request, 'servidores.html', {'servidores': servidores})

def servidor_detalhes(request, id):
    s_detalhe = Servidor.objects.get(id=id)
    return render(request, 'serv-detalhes.html', {'detalhe': s_detalhe})