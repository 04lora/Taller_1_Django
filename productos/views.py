from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Categoria

# ==========================================
# RUTAS DE PRODUCTOS
# ==========================================

def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/listado.html', {'productos': productos})


def registrar_producto(request):
    if request.method == 'POST':
        # Obtener la categoría seleccionada
        cat_id = request.POST['categoria']
        cat = Categoria.objects.get(id=cat_id)

        Producto.objects.create(
            nombre=request.POST['nombre'],
            categoria=cat,  
            precio=request.POST['precio'],
            cantidad=request.POST['cantidad'],
            estado='estado' in request.POST
        )
        return redirect('listar_productos')

    # Si es petición GET, carga el formulario con la lista de categorías
    categorias = Categoria.objects.all()
    return render(request, 'productos/formulario.html', {'categorias': categorias})


def editar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    categorias = Categoria.objects.all()

    if request.method == "POST":
        categoria_id = request.POST.get("categoria")
        producto.categoria = Categoria.objects.get(id=categoria_id) if categoria_id else None
        
        producto.nombre = request.POST.get("nombre")
        producto.precio = request.POST.get("precio")
        producto.cantidad = request.POST.get("cantidad")
        producto.estado = True if request.POST.get("estado") == "on" or 'estado' in request.POST else False
        
        producto.save()
        return redirect('listar_productos')

    return render(request, "productos/formulario.html", {
        "producto": producto,
        "categorias": categorias
    })


def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    return redirect('listar_productos')


# ==========================================
# RUTAS DE CATEGORÍAS
# ==========================================

def listar_categorias(request):
    if request.method == 'POST':
        Categoria.objects.create(
            nombre=request.POST['nombre'],
            descripcion=request.POST['descripcion']
        )
        return redirect('listar_categorias')

    categorias = Categoria.objects.all()
    return render(request, 'productos/categoria_listado.html', {'categorias': categorias})


def editar_categoria(request, id):
    cat = get_object_or_404(Categoria, id=id)
    if request.method == 'POST':
        cat.nombre = request.POST['nombre']
        cat.descripcion = request.POST['descripcion']
        cat.save()
        return redirect('listar_categorias')
    
    return render(request, 'productos/categoria_form.html', {'categoria': cat})


def eliminar_categoria(request, id):
    cat = get_object_or_404(Categoria, id=id)
    cat.delete()
    return redirect('listar_categorias')