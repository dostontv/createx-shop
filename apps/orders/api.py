from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, permissions

from . import serializers
from . import models

@extend_schema(tags=['Carts'])
class CartViewSet(viewsets.ModelViewSet):
    """ViewSet for the Cart class"""

    queryset = models.Cart.objects.all()
    serializer_class = serializers.CartSerializer
    permission_classes = [permissions.IsAuthenticated]

@extend_schema(tags=['Orders'])
class OrderViewSet(viewsets.ModelViewSet):
    """ViewSet for the Order class"""

    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

@extend_schema(tags=['OrderItems'])
class OrderItemViewSet(viewsets.ModelViewSet):
    """ViewSet for the OrderItem class"""

    queryset = models.OrderItem.objects.all()
    serializer_class = serializers.OrderItemSerializer
    permission_classes = [permissions.IsAuthenticated]
