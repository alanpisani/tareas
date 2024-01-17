from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tarea
from django.contrib.auth.decorators import login_required

@login_required

# Create your views here.

def listaDeTareas(request):
    tareas = Tarea.objects.filter(usuario=request.user) #Selecciona todos los cursos de la BD
    data = {"tareas": tareas}
  
    return render(request, "core/home.html", data)

@login_required
def registrarTarea(request):
    conte = request.POST["tarea"]
    usuario_actual = request.user
    tarea = Tarea.objects.create(usuario = usuario_actual, contenido = conte.capitalize(), completado = False)

    return redirect('/')

def borrarTarea(request, id):
    tarea = Tarea.objects.get(id = id)

    tarea.delete()

    return redirect('/')

def tacharTarea(request, id):
    tarea = Tarea.objects.get(id = id)
    tarea.completado = False if tarea.completado else True 

    tarea.save()

    return redirect ('/')

@login_required
def perfil(request):
    return render(request, "account/profile.html")