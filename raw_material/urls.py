from rest_framework import routers
from .api import SupplierView, CategoriesView, RawMaterialView, UnitsView, PaySupplierView, RawMaterialInventoryView

router = routers.DefaultRouter()

router.register('proveedor' , SupplierView, 'proveedor')
router.register('pagosProveedor' , PaySupplierView, 'pagosProveedor')
router.register('categorias', CategoriesView, 'categorias')
router.register('unidades', UnitsView, 'unidades')
router.register('inventario', RawMaterialInventoryView, 'inventarioMateriaPrima')
router.register('', RawMaterialView, 'materiaPrima')

urlpatterns = router.urls