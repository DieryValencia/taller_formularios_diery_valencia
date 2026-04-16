from django.urls import path
from . import views

urlpatterns = [
    path('', views.asistencia_formulario, name='asistencia_formulario'),
    path('confirmacion/', views.asistencia_confirmacion, name='asistencia_confirmacion'),
]