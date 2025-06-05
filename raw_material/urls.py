from rest_framework import routers
from .api import SupplierView, CategoriesView, RawMaterialView, UnitsView

router = routers.DefaultRouter()

router.register('proveedor' , SupplierView, 'proveedor')
router.register('categorias', CategoriesView, 'categorias')
router.register('unidades', UnitsView, 'unidades')
router.register('', RawMaterialView, 'materiaPrima')

urlpatterns = router.urls