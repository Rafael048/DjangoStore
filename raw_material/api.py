from rest_framework import viewsets
from .serializers import SupplierSerializer, CategoriesSerializer, RawMaterialSerializer, UnitsSerializer
from .models import Supplier, Categories, RawMaterial, Units

class SupplierView(viewsets.ModelViewSet):
    serializer_class = SupplierSerializer
    def get_queryset(self):
     queryset = Supplier.objects.filter(eliminado = False)
     eliminado = self.request.query_params.get('eliminados')
     if eliminado: 
        queryset = Supplier.objects.all()
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
     queryset = RawMaterial.objects.select_related('proveedor','categoria', 'unidad').filter(eliminado = False)
     eliminado = self.request.query_params.get('eliminados')
     if eliminado: 
        queryset = RawMaterial.objects.select_related('proveedor','categoria', 'unidad').all()
     return queryset
   
