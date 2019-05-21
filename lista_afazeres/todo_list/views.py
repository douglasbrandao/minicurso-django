from django.shortcuts import render, HttpResponseRedirect
from . models import ItemFazer

def todoView(request):
    todos_afazeres = ItemFazer.objects.all()
    return render(request, 'index.html', {'afazeres': todos_afazeres})

def addTodo(request):
    novo_item = ItemFazer(conteudo = request.POST['conteudo'])
    novo_item.save()
    return HttpResponseRedirect('/todo/')

def deleteTodo(request, id):
    deletar_item = ItemFazer.objects.get(id=id)
    deletar_item.delete()
    return HttpResponseRedirect('/todo/')
