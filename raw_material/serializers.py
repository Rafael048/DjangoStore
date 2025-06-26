from rest_framework import serializers
from .models import RawMaterial, Supplier, Categories, Units, PaySupplier, RawMaterialInventory


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
    
    def update(self, instance, validated_data):
            campo_a_sumar = 'cantidad'  
        
            if campo_a_sumar in validated_data:
                 validated_data[campo_a_sumar] = getattr(instance, campo_a_sumar) + validated_data[campo_a_sumar]
            return super().update(instance, validated_data)

class RawMaterialSerializer(serializers.ModelSerializer):
    inventario = RawMaterialInventorySerializer(read_only=True)
    proveedor = serializers.CharField(source='proveedor.nombre', read_only=True)
    categoria =  serializers.CharField(source='categoria.nombre', read_only=True)
    unidad = serializers.CharField(source='unidad.nombre', read_only=True)
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

