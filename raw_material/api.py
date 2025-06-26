from rest_framework import viewsets
from .serializers import SupplierSerializer, CategoriesSerializer, RawMaterialSerializer, UnitsSerializer, PaySupplierSerializer,RawMaterialInventorySerializer
from .models import Supplier, Categories, RawMaterial, Units, PaySupplier, RawMaterialInventory
class SupplierView(viewsets.ModelViewSet):
    serializer_class = SupplierSerializer
    def get_queryset(self):
     queryset = Supplier.objects.filter(eliminado = False).prefetch_related('pagos')
     eliminado = self.request.query_params.get('eliminados')
     if eliminado: 
        queryset = Supplier.objects.all().prefetch_related('pagos')
     return queryset
    
class PaySupplierView(viewsets.ModelViewSet):
   serializer_class = PaySupplierSerializer
   def get_queryset(self):
      queryset = PaySupplier.objects.filter(eliminado = False)
      eliminado = self.request.query_params.get('eliminados')
      if eliminado:
         queryset = PaySupplier.objects.all()
      return queryset
   
class RawMaterialInventoryView(viewsets.ModelViewSet):
   serializer_class = RawMaterialInventorySerializer
   def get_queryset(self):
      queryset = RawMaterialInventory.objects.filter(eliminado = False)
      eliminado = self.request.query_params.get('eliminados')
      if eliminado:
         queryset = RawMaterialInventory.objects.all()
      return queryset
   
class CategoriesView(viewsets.ModelViewSet):
    serializer_class = CategoriesSerializer
    def get_queryset(self):
     queryset = Categories.objects.filter(eliminado = False)
     eliminado = self.request.query_params.get('eliminados')
     if eliminado: 
        queryset = Categories.objects.all()
     return queryset
    
class UnitsView(viewsets.ModelViewSet):
    serializer_class = UnitsSerializer
    def get_queryset(self):
     queryset = Units.objects.filter(eliminado = False)
     eliminado = self.request.query_params.get('eliminados')
     if eliminado: 
        queryset = Units.objects.all()
     return queryset
    
class RawMaterialView(viewsets.ModelViewSet):
    serializer_class = RawMaterialSerializer
    def get_queryset(self):
     queryset = RawMaterial.objects.filter(eliminado = False).prefetch_related('proveedor','categoria', 'unidad','inventario')
     eliminado = self.request.query_params.get('eliminados')
     if eliminado: 
        queryset = RawMaterial.objects.all().prefetch_related('proveedor','categoria', 'unidad','inventario')
     return queryset
    def perform_create(self, serializer):
        instancia = serializer.save()
        
        RawMaterialInventory.objects.create(
            materiaPrima = instancia,
            cantidad =  0
        )
   
