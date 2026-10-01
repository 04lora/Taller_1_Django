from django.urls import path
from . import views

urlpatterns = [
    # Rutas de Productos
    path('', views.listar_productos, name='listar_productos'),
    path('productos/nuevo/', views.registrar_producto, name='registrar_producto'),
    path('productos/editar/<int:id>/', views.editar_producto, name='editar_producto'),
    path('productos/eliminar/<int:id>/', views.eliminar_producto, name='eliminar_producto'),

    # Rutas de Categorías (Punto 2 del taller)
    path('categorias/', views.listar_categorias, name='listar_categorias'),
    path('categorias/editar/<int:id>/', views.editar_categoria, name='editar_categoria'),
    path('categorias/eliminar/<int:id>/', views.eliminar_categoria, name='eliminar_categoria'),
]