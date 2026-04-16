from django.db import models

class Solicitud(models.Model):
    TIPO_SOLICITUD_CHOICES = [
        ('academica', 'Académica'),
        ('administrativa', 'Administrativa'),
        ('tecnica', 'Técnica'),
        ('otra', 'Otra'),
    ]

    nombre_solicitante = models.CharField(max_length=150)
    documento = models.CharField(max_length=20)  # Alfanumérico
    correo = models.EmailField()
    telefono = models.CharField(max_length=15)  # CharField para manejar guiones y espacios
    tipo_solicitud = models.CharField(max_length=20, choices=TIPO_SOLICITUD_CHOICES)
    asunto = models.CharField(max_length=200)
    descripcion_detallada = models.TextField()
    fecha_solicitud = models.DateField()
    archivo_adjunto = models.FileField(upload_to='solicitudes/', blank=True, null=True)

    def __str__(self):
        return f"{self.nombre_solicitante} - {self.asunto}"
