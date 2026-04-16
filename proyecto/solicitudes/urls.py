from django.urls import path
from . import views

urlpatterns = [
    path('', views.solicitud_formulario, name='solicitud_formulario'),
    path('confirmacion/', views.solicitud_confirmacion, name='solicitud_confirmacion'),
]