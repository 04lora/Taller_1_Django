from django.shortcuts import render, redirect
from .models import Producto

def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/listado.html', {'productos': productos})

def registrar_producto(request):
    if request.method == 'POST':
        Producto.objects.create(
            nombre=request.POST['nombre'],
            categoria=request.POST['categoria'],
            precio=request.POST['precio'],
            cantidad=request.POST['cantidad']
        )
        return redirect('listar_productos')

    return render(request, 'productos/formulario.html')