from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SupplierViewSet, ProductViewSet, StockMovementViewSet, SaleOrderViewSet, ProductStockView

router = DefaultRouter()
router.register(r'suppliers', SupplierViewSet, basename='supplier')
router.register(r'products', ProductViewSet, basename='product')
router.register(r'stockmovements', StockMovementViewSet,
                basename='stockmovement')
router.register(r'saleorders', SaleOrderViewSet,
                basename='saleorder')

urlpatterns = [
    path('', include(router.urls)),
    path('product-stock/', ProductStockView.as_view(), name="product-stock")
]
