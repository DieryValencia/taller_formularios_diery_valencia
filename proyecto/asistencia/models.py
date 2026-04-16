from django.db import models

# Create your models here.

class Asistencia(models.Model):
    nombre_completo = models.CharField(max_length=150)
    documento = models.CharField(max_length=20)  # Alfanumérico, ajusta max_length según necesidad
    correo = models.EmailField()
    fecha_asistencia = models.DateField()
    hora_ingreso = models.TimeField()
    hora_salida = models.TimeField()
    presente = models.BooleanField(default=True)
    observaciones = models.TextField(blank=True)

    def __str__(self):
        return f"{self.nombre_completo} - {self.fecha_asistencia}"
