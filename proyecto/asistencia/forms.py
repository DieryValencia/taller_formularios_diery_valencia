from django import forms
from .models import Asistencia

class AsistenciaForm(forms.ModelForm):
    class Meta:
        model = Asistencia
        fields = '__all__'
        widgets = {
            'fecha_asistencia': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'hora_ingreso': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'hora_salida': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'nombre_completo': forms.TextInput(attrs={'class': 'form-control'}),
            'documento': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
            'presente': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'observaciones': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }