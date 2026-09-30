from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Categoria

# --- PRODUCTOS ---

def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/listado.html', {'productos': productos})

def registrar_producto(request):
    if request.method == 'POST':
        # 1. Obtenemos el ID del formulario y buscamos la instancia de Categoria
        cat_id = request.POST['categoria']
        cat = Categoria.objects.get(id=cat_id)

        Producto.objects.create(
            nombre=request.POST['nombre'],
            categoria=cat,  # Guardamos la instancia, no el texto
            precio=request.POST['precio'],
            cantidad=request.POST['cantidad'],
            estado='estado' in request.POST
        )
        return redirect('listar_productos')

    # 2. Consultamos las categorías y se las enviamos al HTML
    categorias = Categoria.objects.all()
    return render(request, 'productos/formulario.html', {'categorias': categorias})

# Listar y Registrar
def listar_categorias(request):
    if request.method == 'POST':
        Categoria.objects.create(
            nombre=request.POST['nombre'],
            descripcion=request.POST['descripcion']
        )
        return redirect('listar_categorias')

    categorias = Categoria.objects.all()
    return render(request, 'productos/categoria_listado.html', {'categorias': categorias})

# Modificar
def editar_categoria(request, id):
    cat = Categoria.objects.get(id=id)
    if request.method == 'POST':
        cat.nombre = request.POST['nombre']
        cat.descripcion = request.POST['descripcion']
        cat.save()
        return redirect('listar_categorias')
    
    return render(request, 'productos/categoria_form.html', {'categoria': cat})

# Eliminar
def eliminar_categoria(request, id):
    Categoria.objects.get(id=id).delete()
    return redirect('listar_categorias')