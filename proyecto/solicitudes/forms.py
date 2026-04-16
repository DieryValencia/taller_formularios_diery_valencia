from django import forms
from .models import Solicitud

class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = '__all__'
        widgets = {
            'fecha_solicitud': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_solicitud': forms.Select(attrs={'class': 'form-control'}),
            'nombre_solicitante': forms.TextInput(attrs={'class': 'form-control'}),
            'documento': forms.TextInput(attrs={'class': 'form-control'}),
            'asunto': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion_detallada': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'archivo_adjunto': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }