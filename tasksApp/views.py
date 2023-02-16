from django.shortcuts import render, redirect
from .models import Task

# Create your views here.

def task(request):
    tasks = Task.objects.all()
    return render(request, 'task.html', { "tasks": tasks })

def createTask(request):
    task = Task(titulo=request.POST['titulo'], descripcion=request.POST['descripcion'])
    task.save()
    return redirect('/')

def deleteTask(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('/')
