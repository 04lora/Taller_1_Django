from django.db import models

# 1. Creamos el modelo Categoria
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre


# 2. Actualizamos el modelo Producto
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    # Relacionamos Producto con Categoria
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productos')
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.IntegerField()
    # Punto 1 del taller: Atributo estado booleano
    estado = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} - {self.categoria.nombre}"