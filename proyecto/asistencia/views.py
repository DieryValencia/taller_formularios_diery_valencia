from django.shortcuts import render, redirect
from .forms import AsistenciaForm

# Create your views here.

def asistencia_formulario(request):
    if request.method == 'POST':
        form = AsistenciaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('asistencia_confirmacion')
    else:
        form = AsistenciaForm()
    return render(request, 'asistencia/formulario.html', {'form': form})

def asistencia_confirmacion(request):
    return render(request, 'asistencia/confirmacion.html')
