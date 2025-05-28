import django_filter 
from .models import Task, Usuario, Restaurante, Producto, Orden, Repartidor, Calificacion, Notificacion

class TaskFilter(django_filter.FilterSet):
    title = django_filter.CharFilter(lookup_expr='icontains')
    description = django_filter.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Task
        fields = ['title', 'description']

class UsuarioFilter(django_filter.FilterSet):
    nombre = django_filter.CharFilter(lookup_expr='icontains')
    email = django_filter.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Usuario
        fields = ['nombre', 'email']

class RestauranteFilter(django_filter.FilterSet):
    nombre = django_filter.CharFilter(lookup_expr='icontains')
    direccion = django_filter.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Restaurante
        fields = ['nombre', 'direccion']

# Repite este patrón para los otros modelos...