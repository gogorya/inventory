from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Supplier, Product, StockMovement, SaleOrder
from .serializers import SupplierSerializer, ProductSerializer, StockMovementSerializer, SaleOrderSerializer, ProductStockSerializer


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class StockMovementViewSet(viewsets.ModelViewSet):
    queryset = StockMovement.objects.all()
    serializer_class = StockMovementSerializer


class SaleOrderViewSet(viewsets.ModelViewSet):
    queryset = SaleOrder.objects.all()
    serializer_class = SaleOrderSerializer


class ProductStockView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductStockSerializer(products, many=True)
        return Response(serializer.data)
