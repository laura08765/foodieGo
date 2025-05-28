from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q



class Task(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=100)

class Restaurante(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15)

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE)

class Orden(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    productos = models.ManyToManyField(Producto)
    fecha = models.DateTimeField(auto_now_add=True)

class Repartidor(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)

class Calificacion(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE)
    puntuacion = models.IntegerField()
    comentario = models.TextField()

class Notificacion(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    mensaje = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    
class Plato(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=7, decimal_places=2)
    imagen = models.ImageField(upload_to='platos/', blank=True, null=True)
    disponibilidad = models.BooleanField(default=True)




# Método para realizar búsqueda global
def buscar_en_modelos(query):
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

    return resultados

def __str__(self):
    return self.title + '- by ' + self.user.username