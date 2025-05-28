from django.contrib import admin 
from.models import Task, Usuario, Restaurante, Producto, Orden, Repartidor, Calificacion, Notificacion, Plato

class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "created", "datecompleted", "important")
    list_filter = ("important", "user")
    search_fields = ("title", "description")

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ("nombre", "email")
    search_fields = ("nombre", "email")

class RestauranteAdmin(admin.ModelAdmin):
    list_display = ("nombre", "direccion", "telefono")
    search_fields = ("nombre", "direccion")

class ProductoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "precio", "restaurante")
    list_filter = ("restaurante",)
    search_fields = ("nombre",)

class OrdenAdmin(admin.ModelAdmin):
    list_display = ("usuario", "fecha")
    list_filter = ("fecha",)
    search_fields = ("usuario__nombre",)

class RepartidorAdmin(admin.ModelAdmin):
    list_display = ("nombre", "telefono")
    search_fields = ("nombre",)

class CalificacionAdmin(admin.ModelAdmin):
    list_display = ("usuario", "restaurante", "puntuacion")
    list_filter = ("puntuacion", "restaurante")
    search_fields = ("usuario__nombre", "restaurante__nombre")

class NotificacionAdmin(admin.ModelAdmin):
    list_display = ("usuario", "mensaje", "fecha")
    list_filter = ("fecha",)
    search_fields = ("usuario__nombre", "mensaje")


@admin.register(Plato)
class PlatoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'disponibilidad')
    search_fields = ('nombre',)
    list_filter = ('disponibilidad',)

    



admin.site.register(Task, TaskAdmin)
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Restaurante, RestauranteAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Orden, OrdenAdmin)
admin.site.register(Repartidor, RepartidorAdmin)
admin.site.register(Calificacion, CalificacionAdmin)
admin.site.register(Notificacion, NotificacionAdmin)


