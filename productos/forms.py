from django import forms
from .models import Producto, Categoria

# Formulario para registrar y editar Productos (incluye estado)
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'categoria', 'precio', 'cantidad', 'estado']


# Formulario para registrar y editar Categorías (Punto 2)
class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion']