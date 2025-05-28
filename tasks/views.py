from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from  django.db import IntegrityError
from .forms import TaskForm
from .models import Task
from django.db.models import Q
from .models import Task, Usuario, Restaurante, Producto, Orden, Repartidor, Calificacion, Notificacion, Plato




# Create your views here.
def home(request):
    platos = Plato.objects.filter(disponibilidad=True)
    return render(request, 'home.html', {'platos': platos})


def signup(request):

    if request.method == 'GET':
        return render(request, 'signup.html', {
        'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            # registrar usuario
            try:
                user= User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('tasks')
            except IntegrityError :
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    "error": 'el nombre de usuario ya existe'
                })
        return render(request, 'signup.html', {
            'form': UserCreationForm,
            "error": 'La contraseña no coicide'
        })
        
def tasks(request):
    tasks = Task.objects.filter(user=request.user, datecompleted__isnull=True) #se usa para tareas que no estan completadas(pedidos_sin_salir)
    return render(request, 'tasks.html', {'tasks': tasks})

def task_detail(request, task_id):
    tasks = get_object_or_404(Task, pk=task_id)
    return render(request, 'task_detail.html', {'tasks': tasks})

def create_task(request):
    if request.method == 'GET':
        return render(request, 'create_task.html', {
            'form':TaskForm
        })
    else: 
        try:
            form = TaskForm(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'create_task.html', {
            'form':TaskForm,
            'error': 'por favor escribe un dato valido'
        })

def signout(request):
    logout(request)
    return redirect('home')

def signin(request):
    if request.method == 'GET':
        return render (request, 'signin.html',{
            'form': AuthenticationForm
        } )
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'el usuario o la contraseña es incorrecto'
            })
        else:
            login(request, user)
            return redirect('tasks')
        
from django.shortcuts import render




def buscar(request):
    query = request.GET.get("q", "")  
    resultados = []

    if query:
        resultados.extend(Task.objects.filter(Q(title__icontains=query) | Q(description__icontains=query)))
        resultados.extend(Usuario.objects.filter(Q(nombre__icontains=query) | Q(email__icontains=query)))
        resultados.extend(Restaurante.objects.filter(Q(nombre__icontains=query) | Q(direccion__icontains=query)))
        resultados.extend(Producto.objects.filter(Q(nombre__icontains=query)))
        resultados.extend(Orden.objects.filter(Q(usuario__nombre__icontains=query)))
        resultados.extend(Repartidor.objects.filter(Q(nombre__icontains=query) | Q(telefono__icontains=query)))
        resultados.extend(Calificacion.objects.filter(Q(usuario__nombre__icontains=query) | Q(comentario__icontains=query)))
        resultados.extend(Notificacion.objects.filter(Q(usuario__nombre__icontains=query) | Q(mensaje__icontains=query)))

    return render(request, "buscar_resultados.html", {"resultados": resultados, "query": query})

        
        