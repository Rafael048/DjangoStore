from rest_framework import serializers
from .models import RawMaterial, Supplier, Categories, Units


class SupplierSerializer(serializers.ModelSerializer):
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


class RawMaterialSerializer(serializers.ModelSerializer):
    proveedor = SupplierSerializer(read_only=True) 
    categoria = CategoriesSerializer(read_only=True)
    unidad = UnitsSerializer(read_only=True)
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

            
