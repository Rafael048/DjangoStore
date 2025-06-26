from django.db import models

# Create your models here.

class Supplier(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=100)
    telefono = models.CharField(max_length=50)
    codigoTel = models.CharField(max_length=10)
    eliminado = models.BooleanField(default=False)
    creacion = models.DateField(auto_now_add=True)

    
class Categories(models.Model):
    nombre = models.CharField(max_length=100)
    eliminado = models.BooleanField(default=False)
    creacion = models.DateField(auto_now_add=True)

class Units(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    factorBase = models.FloatField()
    eliminado = models.BooleanField(default=False)
    creacion = models.DateField(auto_now_add=True)

class RawMaterial(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.FloatField()
    unidad = models.ForeignKey(Units, on_delete=models.CASCADE)
    proveedor = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categories, on_delete=models.CASCADE)
    eliminado = models.BooleanField(default=False)
    creacion = models.DateField(auto_now_add=True)

class PaySupplier(models.Model):
    fechaPago = models.DateField()
    cantidad = models.FloatField()
    moneda = models.CharField(max_length=50)
    tasa = models.IntegerField()
    referencia = models.CharField(max_length=100)
    proveedor = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='pagos')
    eliminado = models.BooleanField(default=False)
    creacion = models.DateField(auto_now_add=True)

class RawMaterialInventory(models.Model):
    materiaPrima = models.OneToOneField(RawMaterial , on_delete=models.CASCADE, related_name='inventario')
    cantidad = models.FloatField()
    eliminado = models.BooleanField(default=False)
    creacion = models.DateField(auto_now_add=True)