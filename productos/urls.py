from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_productos, name='listar_productos'),
    path('productos/nuevo/', views.registrar_producto, name='registrar_producto'),
]