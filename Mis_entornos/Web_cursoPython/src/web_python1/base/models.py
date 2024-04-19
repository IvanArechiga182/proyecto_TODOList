from django.db import models
from django.contrib.auth.models import User
# Create your models here.

opciones_prioridades = [
    ('alta', 'Alta'),
    ('media', 'Media'),
    ('baja', 'Baja'),
]

class Tarea(models.Model):
    usuario = models.ForeignKey(User, 
                                on_delete=models.CASCADE,
                                null=True,
                                blank=True)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(null=True,
                                    blank=True)
    completo = models.BooleanField(default=False)
    creado = models.DateTimeField(auto_now_add=True)
    fecha_vencimiento = models.DateField(null=True, blank=True)
    prioridad = models.CharField(max_length=10, choices=opciones_prioridades,default='baja')
    materia = models.CharField(max_length=100, default="")

    

    def __str__(self):
        return self.titulo
    
    class Meta:
        ordering = ['completo']
        