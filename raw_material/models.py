from django.db import models

# Create your models here.

class Supplier(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=100)
    telefono = models.CharField(max_length=50)
    eliminado = models.BooleanField(default=False)
    creacion = models.DateField(auto_now_add=True)

    
class Categories(models.Model):
    nombre = models.CharField(max_length=100)
    eliminado = models.BooleanField(default=False)
    creacion = models.DateField(auto_now_add=True)

class Units(models.Model):
    nombre = models.CharField(max_length=100)
    eliminado = models.BooleanField(default=False)
    creacion = models.DateField(auto_now_add=True)

class RawMaterial(models.Model):
    nombre = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    precio = models.FloatField()
    fechaCompra = models.DateField()
    unidad = models.ForeignKey(Units, on_delete=models.CASCADE)
    proveedor = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categories, on_delete=models.CASCADE)
    eliminado = models.BooleanField(default=False)
    creacion = models.DateField(auto_now_add=True)
