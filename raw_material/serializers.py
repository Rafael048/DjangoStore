from rest_framework import serializers
from .models import RawMaterial, Supplier, Categories, Units, PaySupplier, RawMaterialInventory
from django.db.models import Avg, Sum
from django.db import models


class PaySupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaySupplier
        fields = '__all__'
        read_only = ['creacion']
class SupplierSerializer(serializers.ModelSerializer):
    pagos = PaySupplierSerializer(read_only=True, many=True)
    class Meta:
        model = Supplier
        fields = '__all__'
        read_only = ['creacion']
    
class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'
        read_only = ['creacion']

class UnitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Units
        fields = '__all__'
        read_only = ['creacion']

class RawMaterialInventorySerializer(serializers.ModelSerializer):
    class Meta: 
        model = RawMaterialInventory
        fields = '__all__'
        read_only = ['creacion']
    
   

class RawMaterialSerializer(serializers.ModelSerializer):
    inventario = RawMaterialInventorySerializer(read_only=True, many=True)
    proveedor = serializers.CharField(source='proveedor.nombre', read_only=True)
    categoria =  serializers.CharField(source='categoria.nombre', read_only=True)
    unidad = serializers.CharField(source='unidad.nombre', read_only=True)
    factorBase = serializers.FloatField(source='unidad.factorBase', read_only=True)
    precio_promedio = serializers.SerializerMethodField()
    cantidad_total = serializers.SerializerMethodField()
    tipoUnidad = serializers.CharField(source='unidad.tipo', read_only=True)
    proveedor_id = serializers.PrimaryKeyRelatedField(
        queryset=Supplier.objects.all(), 
        source='proveedor', 
        write_only=True
    )
    categoria_id = serializers.PrimaryKeyRelatedField(
        queryset=Categories.objects.all(),
        source='categoria',
        write_only=True
    )
    unidad_id = serializers.PrimaryKeyRelatedField(
        queryset = Units.objects.all(),
        source = 'unidad',
        write_only = True
    )
    class Meta:
        model = RawMaterial
        fields = '__all__'
        read_only = ['creacion']
    
    def validate_cantidad(self, value):
        if value < 0:
              raise serializers.ValidationError({
             'cantidad': 'La cantidad debe ser positiva'
        }) 
            
        return value
    def validate_precio(self, value):
          if value < 0:
              raise serializers.ValidationError({
             'precio': 'La cantidad debe ser positiva'
        })
           
          return value
    def get_precio_promedio(self, obj):
        if hasattr(obj, 'precio_promedio'):
            return obj.precio_promedio
        return round(obj.inventario.filter(eliminado=False).aggregate(
            avg=Avg('precio')
        )['avg'] or 0,2)

    def get_cantidad_total(self, obj):
        if hasattr(obj, 'cantidad_total'):
            return obj.cantidad_total
        return round(obj.inventario.filter(eliminado=False).aggregate(
            total=Sum('cantidad')
        )['total'] or 0,2) 


